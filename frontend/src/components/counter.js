import React, {useState,useEffect} from 'react'
import axios from 'axios';
export default function Counter() {

    const [count,updateCount] = useState(0)
    const [update,setUpdate] = useState(false)

    useEffect( () =>{
        console.log('mounting')
        axios.get()
        .then(res=>{
            updateCount(res.data.count)
        })
        .catch(err => {
            console.error('error found while fetching data',err)
        })
    },[])

    useEffect( () =>{

        if (update){
            console.log("updating count")
            axios.post('')
            .then(res =>{
                updateCount(res.data.count)
                setUpdate(false)
            })
            .catch(err =>{
                console.error('error found while posting count value ',err)
            })
        }
     
    },[update])

    return (
        <div className="counter d-flex justify-content-center align-items-center align-self-center flex-column">
            <p>{count}</p>
            <button onClick={()=>setUpdate(true)}>Increment</button>
        </div>
    )
}
