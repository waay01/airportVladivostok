let coll = document.getElementsByClassName("collapsible"), i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    let content = this.nextElementSibling;
    if (content.style.maxHeight === "0px" || content.style.maxHeight === "") {
      content.style.maxHeight = content.scrollHeight + "px";
    } else {
      content.style.maxHeight = "0px";
    }
  });
}
