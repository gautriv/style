<!-- Email Us Button -->
<button onclick="emailUs()">Email Us</button>

<!-- Optional Note -->
<p>If the button doesn't work, you can email us directly at <strong>support@example.com</strong>.</p>

<!-- JavaScript Code -->
<script>
function emailUs() {
    var mailtoLink = 'mailto:support@example.com?subject=Customer%20Inquiry';
    var gmailLink = 'https://mail.google.com/mail/?view=cm&fs=1&to=support@example.com&su=Customer%20Inquiry';

    // Try to open the mailto link
    window.location.href = mailtoLink;

    // After a short delay, check if the user is still on the page
    setTimeout(function() {
        if (document.hasFocus()) {
            // Mailto link didn't work, open Gmail in a new tab
            var opened = window.open(gmailLink, '_blank');
            if (!opened) {
                alert('Please allow pop-ups for this website to use your web-based email service.');
            }
        }
    }, 1000);
}

// Prompt users to set Gmail as the handler for mailto links
if (navigator.registerProtocolHandler) {
    navigator.registerProtocolHandler(
        'mailto',
        'https://mail.google.com/mail/?extsrc=mailto&url=%s',
        'Gmail'
    );
}
</script>
