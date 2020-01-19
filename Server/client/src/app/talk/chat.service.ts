import { Injectable, Inject } from '@angular/core';
import { Observable } from 'rxjs';
import { Message } from '../interfaces/Message'
import { HttpClient } from '@angular/common/http';
import { DOCUMENT } from '@angular/common'

import * as io from 'socket.io-client';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ChatService {
  socket: SocketIOClient.Socket;

  constructor(private httpClient: HttpClient,
              @Inject(DOCUMENT) private document: Document) {
      this.socket = io(environment.SOCKET_ENDPOINT);

      this.socket.on('connection', function(socket){
        console.log('Connected');
      });
  }

  sendMessage(msgObj) {
    this.socket.emit("message", JSON.stringify(msgObj));
  }
  
  getResponseObservable(): Observable<Object>{
    // return this.socket.fromEvent("message");
    return new Observable<Object>((observer) => {
      this.socket.on("message", (data) => {
        console.log(data["body"])
        observer.next(JSON.parse(data));
      });
    });
  }

  getHistory(): Observable<Object> {
    return this.httpClient.get(`http://${this.document.location.host}/messages/b`);
  }
}
