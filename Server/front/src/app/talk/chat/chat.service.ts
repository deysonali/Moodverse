import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';

import { map } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { BehaviorSubject } from 'rxjs';

export class Message {
  constructor(public content: string, public sentBy: string) {}
}



@Injectable()
export class ChatService {
  //conversation = new BehaviorSubject<Message[]>([]);
  socket;
  constructor() { // Create WebSocket connection.
        this.socket = new WebSocket('ws://localhost:8080');
        this.socket.addEventListener('open', function (event) {
            this.socket.send('Hello Server!');
        });
   }

  send(userMessage: String){
  if (this.socket.readyState === 1)
  this.socket.send(userMessage);
  }

  getMessageListener(){
     return new Observable((observer) => {
      this.socket.onMessage = function(data){
      observer.next(JSON.parse(data));
      }
      });
     }
  }


