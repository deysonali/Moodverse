import { Component, OnInit,} from '@angular/core';
import { ChatService } from './chat.service';


@Component({
  selector: 'app-talk',
  templateUrl: './talk.component.html',
  styleUrls: ['./talk.component.css']
})
export class TalkComponent implements OnInit {
  messages = [];
  date = new Date();
  txtInput = "";

  constructor(private chatService: ChatService) { }

  ngOnInit() {
    this.chatService.getResponseObservable().subscribe(data => {
      this.messages.unshift({
        author_id: "Mood Bot",
        body: data["body"],
        sent: "2020-01-19",
      });
    });
  }

  public sendMessage() {
    this.messages.unshift({
      author_id: "John",
      body: this.txtInput,
      sent: "2020-01-19",
    });
    this.chatService.sendMessage({
      author_id: "John",
      body: this.txtInput,
      sent: new Date(),
      type: 0,
    })
    this.txtInput = "";
  }

}
