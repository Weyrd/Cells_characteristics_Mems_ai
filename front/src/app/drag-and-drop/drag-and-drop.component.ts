import { Component } from '@angular/core';

@Component({
  selector: 'app-drag-and-drop',
  templateUrl: './drag-and-drop.component.html',
  styleUrls: ['./drag-and-drop.component.css']
})
export class DragAndDropComponent {
  images: string[] = []; // Array to store image URLs
  isFileOverContainer: boolean = false;
  isFileDragging: boolean = false;

  onDragStart(event: DragEvent, image: string): void {
    event.dataTransfer?.setData('text/plain', image);
  }

  onDragOverContainer(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.isFileOverContainer = true;
  }

  onDragOver(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.isFileDragging = true;
  }
  onDragLeave(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.isFileOverContainer = false;
    this.isFileDragging = false;

  }

  onDrop(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.isFileOverContainer = false;
    this.isFileDragging = false;


    const files = event.dataTransfer?.files;
    if (files && files.length > 0) {
      const file = files[0];
      this.readFile(file);

    }
  }

  onFileChange(event: Event): void {
    const target = event.target as HTMLInputElement;
    const files = target.files;
    if (files && files.length > 0) {
      const file = files[0];
      this.readFile(file);
    }
  }

  private readFile(file: File): void {
    const reader = new FileReader();
    reader.onload = (e: ProgressEvent<FileReader>) => {
      const imageUrl = e.target?.result as string;
      this.images.push(imageUrl);
    };
    reader.readAsDataURL(file);
  }

  // Rest of your component code
}
