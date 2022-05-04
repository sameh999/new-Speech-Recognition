import RecorderControls from "./components/recorder-controls";
import RecordingsList from "./components/recordings-list";
import useRecorder from "./hooks/useRecorder";
import "./app.css";

import {useState, useEffect} from 'react';
import {Deploy} from './components/deploy/deploy';


export default function App() {
  const { recorderState, ...handlers } = useRecorder();
  const { audio } = recorderState;


  const [state, setState] = useState({})

  useEffect(() => {
    fetch("/api").then(response => {
      if(response.status === 200){
        const parsedResponse = JSON.parse(response);
        console.log(parsedResponse.name);
        return ( <h1> {response.data['transcript']} </h1> )  // 
      }
    }).then(data => setState(data))
    .then(error => console.log(error))
  },[])

  
  return (
    <><h1 className='app_header'>Transcribe your voice to text </h1>
      <section className="voice-recorder">
        <h1 className="title">Voice Recorder</h1>
        <div className="recorder-container">
          <RecorderControls recorderState={recorderState} handlers={handlers} />
          <RecordingsList audio={audio} />
        </div>
      </section>

      <div className="speechContainer">

        <h3>Upload your .wav file</h3>
        <form method="post" action="\api" encType="multipart/form-data">
          <input type="file" name="file" />
          <br />
          <h3>Convert audio to text </h3>
          <input type="submit" id="submitButton" defaultValue="Transcribe" />

        </form>


        <div id="speechTranscript">
          <div id="speechTranscriptContainer">
            <h1>Results</h1>
            <p id="speechText">
              { state.transcript }
              {/* <Deploy prop={state} /> */}
            </p>
          </div>  
        </div>
      </div></>
  );
  }
