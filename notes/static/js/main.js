document.addEventListener("DOMContentLoaded", () => {
  const formCon = document.getElementById('todo-form')
  const form = document.getElementById('noteForm')
  const openBtn = document.getElementById('openForm')
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
  
})