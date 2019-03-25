window.onload = afterLoad()

function update_success_messages(){
    success_messages = document.getElementsByClassName('success')
    // console.log('ran')
    // console.log(success_messages)
    for (success_message of success_messages) { 
        console.log('ran again')
        console.log(success_message)
        // success_message.addeventlistener('click', closeMessage)
        success_message.onclick = function() {this.parentNode.removeChild(this);}
    }
}
function update_local_time(){
    time = new Date(document.getElementById('observation-table').dataset.ztime)
    console.log(time)
    local_time_placeholder = document.getElementById('observation-localtime')
    local_time_placeholder.innerHTML = "Local: " + time.toLocaleString()
}

function afterLoad(){
    update_success_messages()
    update_local_time()
}
