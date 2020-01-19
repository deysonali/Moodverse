import { RouterModule, Routes } from '@angular/router';
import { AppRoutingModule } from './app-routing.module';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { AboutComponent } from './about/about.component';
import { InsightsComponent } from './insights/insights.component';
import { TalkComponent } from './talk/talk.component';
import { HomeComponent } from './home/home.component';
import { NgModule } from '@angular/core';
import { ChatDialogComponent } from './talk/chat/chat-dialog/chat-dialog.component';
import { ChatService, Message } from './talk/chat/chat.service';
import { map } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
//import { ApiAiClient } from 'api-ai-javascript';
import { FormsModule } from '@angular/forms';
import * as SockJS from 'sockjs-client';

@NgModule({
  declarations: [
    AppComponent,
    AboutComponent,
    InsightsComponent,
    TalkComponent,
    HomeComponent,
    ChatDialogComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [ChatService],
  bootstrap: [AppComponent]
})
export class AppModule { }
