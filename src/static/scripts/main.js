console.log("here")

function handleTitleMove(id, ownid, offset) {
        if ( (offset===28)||offset===6&&document.getElementById(ownid).value==="")
        document.getElementById(id).style.bottom=`${offset}px`
        console.log("kalja")
    }
    
    let fieldData = [
        ["Otsikko", "title"],
        ["Linkki", "link_url"]
    ]
    function createFields(arr, parentId) {
        let parent = document.getElementById(parentId)
        parent.classList.add()
        arr.forEach(elem => {
            let newElement = document.createElement("div")
            newElement.classList.add("input-container")
            newElement.innerHTML=`
            <input name="${elem[1]}" id="${elem[1]}" onfocus="handleTitleMove('${elem[1]}-title', '${elem[1]}', 28)" onblur="handleTitleMove('${elem[1]}-title', '${elem[1]}', 6)"></input>
            <h3 id="${elem[1]}-title">${elem[0]}</h3>`
            parent.appendChild(newElement)
        })
    }
window.onload=()=>createFields(fieldData, "form-input-container")