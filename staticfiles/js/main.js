document.addEventListener("DOMContentLoaded", () => {
  const formCon = document.getElementById('todo-form')
  const form = document.getElementById('noteForm')
  const openBtn = document.getElementById('openForm')
  const closeBtn = document.getElementById('closeForm')
  const notes = document.querySelectorAll('.notes')
  
  openBtn.addEventListener('click', (e) => {
    formCon.style.left = '0'
    formCon.style.transition = 'all 0.3s'
    e.target.style.display = 'none'
  })
  
  closeBtn.addEventListener('click', (e) => {
    formCon.style.left = '-200%'
    formCon.style.transition = 'all 0.3s'
    openBtn.style.display = 'block'
  })
  
  notes.forEach(note => {
    const id = note.getAttribute('data-file-id')
    note.addEventListener("click", () => {
      
    })
  })
  
})