css = '''
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: flex-start;
    gap: 1rem;
}
.chat-message.user {
    background-color: #2b313e;
}
.chat-message.bot {
    background-color: #475063;
}
.chat-message .avatar {
    flex-shrink: 0;
}
.chat-message .avatar img {
    max-width: 64px;
    max-height: 64px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #fff;
}
.chat-message .message {
    flex-grow: 1;
    color: #fff;
    font-size: 1rem;
    line-height: 1.4;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" alt="Bot Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png" alt="User Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
