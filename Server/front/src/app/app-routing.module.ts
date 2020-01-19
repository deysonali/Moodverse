import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {AboutComponent} from './about/about.component';
import {InsightsComponent} from './insights/insights.component';
import {HomeComponent} from './home/home.component';
import {TalkComponent} from './talk/talk.component';

const routes: Routes = [
{path:'',component:HomeComponent},
{path: 'talk', component:TalkComponent},
{path: 'about', component:AboutComponent},
{path: 'insights', component:InsightsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
