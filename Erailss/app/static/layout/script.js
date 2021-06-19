const imgs = document.querySelectorAll('.img-select a');
console.log("aaaaaaa+++",imgs)
const imgBtns = [...imgs];
console.log("aaaaaaa+++imgBtns++",imgBtns)
let imgId = 1;

imgBtns.forEach((imgItem) => {
    imgItem.addEventListener('click', (event) => {
        event.preventDefault();
        console.log("aaaaaaa+++imgItem.dataset.id++",imgItem.dataset.id)
        imgId = imgItem.dataset.id;
        slideImage();
    });
});

function slideImage(){
    const displayWidth = document.querySelector('.img-showcase img:first-child').clientWidth;

    document.querySelector('.img-showcase').style.transform = `translateX(${- (imgId - 1) * displayWidth}px)`;
}

window.addEventListener('resize', slideImage);


function clickme(smallImg) {

    var fullImg = document.getElementById("imagebox");
    fullImg.src = smallImg.src;

}