import { Component } from '@angular/core';
import { ApiService } from './api.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent {
  posts = [{id:1,title:'Just example', content: 'Something', author: 'admin'},{id:2,title:'An example', content: "Really something",author: 'admin'}];
  constructor(private api:ApiService) {
    this.getPosts();
  }
  getPosts = () => {
    this.api.getAllPosts().subscribe (
      (data: any) => {
        console.log(data);
        this.posts = data; //data.results;
      },
      (error: any) => {
        console.log(error);
      } 
      ) 
    }
} 
      