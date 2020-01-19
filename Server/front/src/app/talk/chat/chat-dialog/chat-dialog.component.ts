import { Component, OnInit } from '@angular/core';
import { ChatService, Message } from '../chat.service';
import { map } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';

@Component({
  selector: 'chat-dialog',
  templateUrl: './chat-dialog.component.html',
  styleUrls: ['./chat-dialog.component.css']
})
export class ChatDialogComponent implements OnInit {

  messages;
  formValue: string;

  constructor(public chat: ChatService) { }

  ngOnInit() {
      const myObserver = {
        next: x => {
          console.log('Observer got a next value: ' + x)
         this.messages.push(x)
        },
        error: err => {
          console.error('Observer got an error: ' + err)
        },
        complete: () => {
          console.log('Observer got a complete notification')
        },
      };
      // appends to array after each new message is added to feedSource
      this.chat.getMessageListener().subscribe(myObserver);
  }
  sendMessage() {
    this.chat.send(this.formValue);
    this.formValue = 'Im user message';
  }
}
