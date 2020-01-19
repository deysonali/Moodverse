import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TalkComponent } from './talk.component';

describe('TalkComponent', () => {
  let component: TalkComponent;
  let fixture: ComponentFixture<TalkComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TalkComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TalkComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
   it(`should have as title 'talk'`, async(() => {
      const fixture = TestBed.createComponent(TalkComponent);
      const talk = fixture.debugElement.componentInstance;
      expect(app.title).toEqual('talk');
    }));
    it('should render title in a h1 tag', async(() => {
      const fixture = TestBed.createComponent(TalkComponent);
      fixture.detectChanges();
      const compiled = fixture.debugElement.nativeElement;
      expect(compiled.querySelector('h1').textContent).toContain('Welcome to app!');
    }));
});
