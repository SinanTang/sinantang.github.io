// Hide the pageviews counter while keeping GoatCounter analytics active
document.addEventListener('DOMContentLoaded', function() {
  const pageviewsElement = document.getElementById('pageviews');
  if (pageviewsElement) {
    // Hide the parent span that contains both the pageviews element and "views" text
    const parentSpan = pageviewsElement.closest('span');
    if (parentSpan) {
      parentSpan.style.display = 'none';
    }
  }
});