$(document).ready(function() {
  // Form validation for add/edit pages
  $('#questionForm').on('submit', function(e) {
    const form = this;
    if (!form.checkValidity()) {
      e.preventDefault();
      e.stopPropagation();
    }
    form.classList.add('was-validated');
  });

  // Delete confirmation modal
  let deleteId = null;
  $('.btn-delete').on('click', function() {
    deleteId = $(this).data('id');
    const title = $(this).data('title');
    $('#deleteItemTitle').text(title);
    $('#deleteForm').attr('action', `/delete/${deleteId}`);
    const modal = new bootstrap.Modal(document.getElementById('confirmDeleteModal'));
    modal.show();
  });

  // Toggle solved status
  $('.btn-toggle').on('click', function() {
    const btn = $(this);
    const id = btn.data('id');
    $.post(`/toggle_solved/${id}`, function(data) {
      if (data.ok) {
        const row = btn.closest('tr');
        const badge = row.find('.solved-badge');
        if (data.solved) {
          badge.removeClass('bg-secondary').addClass('bg-success').text('Solved');
          btn.text('Mark Unsolved');
          row.addClass('solved').removeClass('unsolved');
        } else {
          badge.removeClass('bg-success').addClass('bg-secondary').text('Unsolved');
          btn.text('Mark Solved');
          row.addClass('unsolved').removeClass('solved');
        }
      }
    });
  });

  // Live filtering and search on questions page
  function filterTable() {
    const searchVal = $('#searchInput').val().toLowerCase();
    const diffVal = $('#difficultyFilter').val();
    const compVal = $('#companyFilter').val();
    const tagVal = $('#tagFilter').val().toLowerCase();

    $('#questionsTable tbody tr').each(function() {
      const row = $(this);
      const title = row.data('title');
      const company = row.data('company');
      const tags = row.data('tags');
      const difficulty = row.data('difficulty');

      let show = true;

      // Search filter
      if (searchVal && !title.includes(searchVal) && !company.includes(searchVal) && !tags.includes(searchVal)) {
        show = false;
      }

      // Difficulty filter
      if (diffVal && difficulty !== diffVal) {
        show = false;
      }

      // Company filter
      if (compVal && company !== compVal.toLowerCase()) {
        show = false;
      }

      // Tag filter
      if (tagVal && !tags.includes(tagVal)) {
        show = false;
      }

      row.toggle(show);
    });
  }

  $('#searchInput, #difficultyFilter, #companyFilter, #tagFilter').on('input change', filterTable);
});
