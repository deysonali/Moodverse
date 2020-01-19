import { Component, OnInit } from '@angular/core';
import { ChatService } from './talk/chat.service';
import { Message } from './interfaces/Message'
import { NgModel } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  messages: Message[] = [];

  txtInput: string = "";

  constructor(private cs: ChatService) { }

  ngOnInit() {
    this.cs.getHistory().subscribe({
      next: msg => {
        console.log('Recieved message in app');
        for (let key in msg) {
          let temp: Message = {
            author_id: msg[key]["author_id"],
            message_id: msg[key]["message_id"],
            type: msg[key]["type"],
            body: msg[key]["body"],
            sent: new Date(msg[key]["sent"])
          }
          this.messages.push(temp)
        }
      },
      error(e) {
        console.log('Error recieving message in app: ', e);
      }
    });
  }

  sendMessage() {
    let temp: Message = {
      author_id: "D",
      message_id: "D",
      type: 1,
      body: this.txtInput,
      sent: new Date()
    }
    this.messages.push(temp)
    this.cs.sendMessage(temp)
  }
}
