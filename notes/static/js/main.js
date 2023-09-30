document.addEventListener("DOMContentLoaded", () => {
  const formCon = document.getElementById('todo-form')
  const form = document.getElementById('noteForm')
  const editForm = document.querySelectorAll('.editForm')
  const openBtn = document.getElementById('openForm')
  const submitBtn = document.getElementById('submitBtn')
const editBtn = document.querySelectorAll('.editBtn')
  const closeBtn = document.getElementById('closeForm')
  const closeDetail = document.getElementById('closeDetail')
  const detailCon = document.getElementById('detail-con')
  const notes = document.querySelectorAll('.notes')
  const deleteBtn = document.querySelectorAll('.delete')
  const detailTitle = document.querySelector('.detail-t')
  const detailContent = document.querySelector('.detail-b')
  
  openBtn.addEventListener('click', (e) => {
    formCon.style.left = '0'
    formCon.style.transition = 'all 0.3s'
    e.target.style.display = 'none'
    openBtn.style.display = 'none'
  })
  
  closeBtn.addEventListener('click', (e) => {
    formCon.style.left = '-200%'
    formCon.style.transition = 'all 0.3s'
    openBtn.style.display = 'block'
  })
  
  closeDetail.addEventListener("click", () => {
    detailCon.classList.add('hidden')
  })
  
  deleteBtn.forEach(btn => {
    const noteId = btn.getAttribute('data-file-del')
    btn.addEventListener("click", () => {
      const url = `/delete/${noteId}`
      
      fetch(url)
      .then(res => res.json())
      .then(data => {
        setTimeout(function() {
          window.location.reload()
        }, 1600);
        alert(data.message)
      }).catch(error => {
        alert(error)
      })
    })
  })
  
  notes.forEach(note => {
    const id = note.getAttribute('data-file-id')
    note.addEventListener("click", () => {
      const url = `/detail/${id}`
      fetch(url)
      .then(response => response.json())
      .then(data => {
        detailCon.classList.toggle('hidden')
        detailTitle.textContent = data.title
        detailContent.innerHTML = data.content
//         alert(data.title)
       })
       .catch(error => {
         alert(error)
       })
    })
  })
  
  noteForm.addEventListener('submit', (e) => {
    e.preventDefault()
    const formElement = e.target
    const formData = new FormData(formElement)
    const url = 'https://notepad-fl.onrender.com/'
    
    fetch(url, {
      method: 'POST',
      body: formData
    })
    .then(res => res.json())
    .then(data => {
      submitBtn.textContent = data.message;
      setTimeout(function() {
        formCon.style.left = '-200%'
        formCon.style.transition = 'all 0.3s'
        openBtn.style.display = 'block'
      }, 2000);
      formElement.reset()
      
      setTimeout(function() {
         window.location.reload()
       }, 2300);
    })
    .catch(error => {
      alert(error)
    })
  })
  

editForm.forEach(form => {
  form.addEventListener('submit', (e) => {
    e.preventDefault()
    const formElement = e.target
    const id = e.target.getAttribute('data-note-id')
    const formData = new FormData(formElement)
    const url = `/edit/${id}/`
    
    fetch(url, {
      method: 'POST',
      body: formData
    })
    .then(res => res.json())
    .then(data => {
      editBtn.forEach(btn => {
       btn.textContent = data.message;
      })
      setTimeout(function() {
        closeModal(`modal-${id}`)
      }, 1500);

       setTimeout(function() {
         window.location.reload()
       }, 2000);
    })
    .catch(error => {
      alert(error)
    })
})
})

  
})

