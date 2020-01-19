import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';

import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { AboutComponent } from './about/about.component';
import { HomeComponent } from './home/home.component';
import { InsightsComponent } from './insights/insights.component';
import { TalkComponent } from './talk/talk.component';

import { RouterModule, Routes } from '@angular/router';

const appRoutes: Routes = [
  {path:'',component:TalkComponent},
  ];

@NgModule({
  declarations: [
    AppComponent,
    AboutComponent,
    HomeComponent,
    InsightsComponent,
    TalkComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(
      appRoutes,
      { enableTracing: true } // <-- debugging purposes only
    ),
    HttpClientModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
