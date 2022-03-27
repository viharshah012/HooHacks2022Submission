import React, { useState, useEffect } from 'react'

function App() {
  
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/members").then(
        res => res.json()
    ).then(
        data => {
          setData(data)
          console.log(data)
        }
    )
  }, [])

  return (
      <div style="background-color:LightGray;">
          {(typeof data.members === 'undefined') ? (
              <p></p>
          ): (
            data.members.map((member, i) => (
              <p key={i}><a href={member}>Link {i}</a></p>
            ))
          )}
      </div>
      
  )
}

export default App