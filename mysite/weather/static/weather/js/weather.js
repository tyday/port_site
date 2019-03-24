window.onload = afterLoad()



function afterLoad(){
    success_messages = document.getElementsByClassName('success')
    console.log('ran')
    console.log(success_messages)
    for (success_message of success_messages) { 
        console.log('ran again')
        console.log(success_message)
        // success_message.addeventlistener('click', closeMessage)
        success_message.onclick = function() {this.parentNode.removeChild(this);}
    }
}