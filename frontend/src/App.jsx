import React, { useState, useEffect } from 'react';
import AceEditor from 'react-ace';
import "ace-builds/src-noconflict/theme-monokai";
import ace from 'ace-builds/src-noconflict/ace';
import './mode-szprajch';


function App() {
  const [code, setCode] = useState('ZMIYNNO x = 2');
  const [output, setOutput] = useState('');

  useEffect(() => {
    const editor = ace.edit("szprajch-editor");
    editor.session.setMode("ace/mode/szprajch");
  }, []);

  const runCode = async () => {
    setOutput('⏳ Uruchamianie...');
    try {
      const response = await fetch('http://localhost:5000/run', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ code }),
      });

      const result = await response.json();
      if (result.error) {
        setOutput("Błąd: " + result.error);
      } else {
        // setOutput("✅ " + result.output + "\n\n" + JSON.stringify(result.variables, null, 2) + "\n\n" + result.result);
        setOutput(result.output + "\n\n" + result.result);
      }
    } catch (err) {
      setOutput("❌ Błąd połączenia z backendem");
    }
  };

  return (
    <div style={{ display: 'flex', height: '100vh' }}>
      <div style={{ width: '50%', padding: '10px' }}>
        <AceEditor
          mode="szprajch" 
          theme="monokai"
          value={code}
          onChange={setCode}
          name="szprajch-editor"
          editorProps={{ $blockScrolling: true }}
          width="100%"
          height="90%"
        />
        <button onClick={runCode}>Run</button>
      </div>
      <div style={{ width: '50%', padding: '10px', background: '#eee' }}>
        <pre>{output}</pre>
      </div>
    </div>
  );
}

export default App;
