import {Component, Output, EventEmitter} from '@angular/core';

@Component({
  selector: 'app-drag-and-drop',
  templateUrl: './drag-and-drop.component.html',
  styleUrls: ['./drag-and-drop.component.css']
})
export class DragAndDropComponent {
  @Output() addImage = new EventEmitter<any>();

  isFileOverContainer: boolean = false;
  isFileDragging: boolean = false;


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
    const filesList: File[] = [];
    if (files) {
      for (let i = 0; i < files.length; i++) {
        filesList.push(files[i]);
      }
      this.readFile(filesList);
    }
  }


  private readFile(files: File[]): void {
    files.forEach((file: File) => {
      const reader = new FileReader();

      reader.onload = (e: ProgressEvent<FileReader>) => {
        const imageUrl = e.target?.result as string;

        const img = new Image();
        img.onload = () => {
          const imageSize = {
            width: img.width,
            height: img.height
          };
          let image = {"url": imageUrl, "size": imageSize}
          this.addImage.emit(image);
          console.log("image", image)

        };
        img.src = imageUrl;

      };
      reader.readAsDataURL(file);

    });

  }

}
