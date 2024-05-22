setInterval(setClock,1000);//it is used to call the set clock function every 1000 miliseconds that is 1 second
const hourhand = document.querySelector('[data-hour-hand]');//query select data attributes
const minutehand = document.querySelector('[data-minute-hand]');
const secondhand = document.querySelector('[data-second-hand]');

function setClock()
{
    const currentDate = new Date();//gets the current time using Date() constructor
    const secondsRatio = currentDate.getSeconds()/60;//360 degree ma second hand lai 60 choti rotate garaunu paro
    const minutesRatio = (secondsRatio + currentDate.getMinutes())/60;
    const hoursRatio = (minutesRatio + currentDate.getHours())/12;
    /*calculates the position of each hand by dividing the number of seconds, minutes,
    and hours by 60 or 12 to get the ratio of each hand's position to a full rotation (360 degrees).*/
    setrotation(secondhand,secondsRatio);
    setrotation(minutehand,minutesRatio);
    setrotation(hourhand,hoursRatio);


}
/**The setrotation() function sets the CSS custom property 
* --rotation on the element to the product of the rotation ratio and 360 degrees. */
function setrotation(element,rotationratio)
{
    element.style.setProperty('--rotation',rotationratio * 360)
}
setClock()