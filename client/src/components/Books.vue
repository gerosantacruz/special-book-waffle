<template>
    <!-- eslint-disable max-len -->
    <div class="container">
        <div class="row">
            <div class="col-sm-10">
                <h1>Books</h1>
                <hr><br><br>
                <button type="button" class="btn btn-success btn-sm">Add Books</button>
                <br><br>
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">Title</th>
                            <th scope="col">Author</th>
                            <th scope="col">Read?</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(book,index) in books" :key="index">
                            <td>{{book.title}}</td>
                            <td>{{book.author}}</td>
                            <td>
                                <span v-if="book.read">Yes</span>
                                <span v-else>No</span>
                            </td>
                            <td>
                                <div class="btn-group" role="group">
                                    <button type="button" class="btn btn-warning btn-sm">Update</button>
                                    <button type="button" class="btn btn-danger btn-sm">Warnin</button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <b-modal ref="addBookModal" id="book-modal" title="add a new book" hide-footer>
          <b-form class="w-100" @submit="onSubmit" @reset="onReset">
            <b-form-group id="form-title-group" label="Title:" label-for="form-title-input">
              <b-form-input id="form-title-input" type="text" v-model="addBookForm.title" placeholder="Enter Title" required>
              </b-form-input>
            </b-form-group>
            <b-form-group id="form-author-group" label="Author:" label-for="form-author-input">
              <b-form-input id="form-author-input" type="text" v-model="addBookForm.author" placeholder="Enter Author" required>
              </b-form-input>
            </b-form-group>
            <b-form-group id="form-read-group">
              <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
                <b-form-checkbox value="true">Read?</b-form-checkbox>
              </b-form-checkbox-group>
              <b-button type="submit" variant="primary">Submit</b-button>
              <b-button type="reset" variant="danger">Reset</b-button>
            </b-form-group>
          </b-form>
        </b-modal>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      books: [],
    };
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // esLint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
