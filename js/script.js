var i = 0;
var original = document.getElementById("grid");
function duplicate() {
    var clone = this.cloneNode(true); // "deep" clone
    clone.id = "grid" + ++i; // there can only be one element with an ID
    clone.onclick = duplicate; // event handlers are not cloned
    this.parentNode.appendChild(clone);
}
