const todos = document.querySelectorAll(".todo");
const all_status = document.querySelectorAll(".status");
let draggableTodo = null;

// DRAG AND DROP SYSTEM !

todos.forEach((todo) => {
  todo.addEventListener("dragstart", dragStart);
  todo.addEventListener("dragend", dragEnd);
});

function dragStart() {
  draggableTodo = this;
  setTimeout(() => {
    this.style.display = "none";
  }, 0);
}

function dragEnd() {
  draggableTodo = null;
  setTimeout(() => {
    this.style.display = "block";
  }, 0);
}

all_status.forEach((status) => {
  status.addEventListener("dragover", dragOver);
  status.addEventListener("dragenter", dragEnter);
  status.addEventListener("dragleave", dragLeave);
  status.addEventListener("drop", dragDrop);
});

function dragOver(e) {
  e.preventDefault();
}

function dragEnter() {
  this.style.border = "1px dashed #ccc";
}

function dragLeave() {
  this.style.border = "none";
}

function dragDrop() {
  this.style.border = "none";
  this.appendChild(draggableTodo);
}

// ADD TASK OR SUBTASK

const add_Task = document.getElementById("addTask");


function createTask() {
    const add_Task = document.createElement("div");
    const input_text = document.getElementById("inputField").value;
    const text = document.createTextNode(input_text);

    add_Task.appendChild(text);
    add_Task.classList.add("todo");
    add_Task.setAttribute("draggable", "true");

    // Remove button SPAN

  const span = document.createElement("span");
  const span_txt = document.createTextNode("\u00D7");
  span.classList.add("close");
  span.appendChild(span_txt);

  add_Task.appendChild(span);
  addInputToInterface.appendChild(add_Task);

  span.addEventListener("click", () => {
  span.parentElement.style.display = "none";
  });
    addInputToInterface.appendChild(add_Task);

    console.log(add_Task);

    add_Task.addEventListener("dragstart", dragStart);
    add_Task.addEventListener("dragend", dragEnd);

    document.getElementById("inputField").value ="";

}
 const close_btns = document.querySelectorAll(".close");

close_btns.forEach((btn) => {
  btn.addEventListener("click", () => {
    btn.parentElement.style.display = "none";
  });
});


//Source inspired by Basir Payenda (Source dans le rapport)
//Source inspired by W3School (Source dans le rapport)


// SAVE PAGE STATE (LOCALSTORAGE)

  // this line isn't really necessary here but you have to append this attribute to the element you want the html stored of.
 /* $("#wrapper").attr("contenteditable", "true")

  var content = document.getElementById('wrapper');

  // save the page's state after you're done with editing and clicked outside the content
  $(content).blur(function() {
    localStorage.setItem('status_html', this.innerHTML);  //Store
  });

  // pretty logical, getItem retrieves your local storage data
  if (localStorage.getItem('status_html')) {
    content.innerHTML = localStorage.getItem('status_html'); // Retrieve
  }

}); */



function clickReset(){

    localStorage.clear();
    window.location = window.location;

    console.log("reset page");

}


// Source W3School and Basir Payenda (Source complet dans le rapport)