const translations = {
    'en': {
      'home': 'Home',
      'about': 'About Us',
      'projects': 'Our Projects',
      'transparency': 'Transparency',
      'donate': 'Donate',
      'contact': 'Contact',
      'mission': 'Our Mission',
      'leadership': 'CELID Leadership',
      'history': 'Our History',
      'partners': 'Partners',
      'document': 'Document'
    },
    'fr': {
      'home': 'Accueil',
      'about': 'À propos',
      'projects': 'Nos Projets',
      'transparency': 'Transparence',
      'donate': 'Faire un don',
      'contact': 'Contact',
      'mission': 'Notre Mission',
      'leadership': 'Direction CELID',
      'history': 'Notre Histoire',
      'partners': 'Partenaires',
      'document': 'Document'
    },
    'rw': {
      'home': 'Ahabanza',
      'about': 'Ibyerekeye',
      'projects': 'Ibikorwa',
      'transparency': 'Ubwirabire',
      'donate': 'Tanga',
      'contact': 'Twandikire',
      'mission': 'Intego yacu',
      'leadership': 'Abayobozi ba CELID',
      'history': 'Amateka yacu',
      'partners': 'Abafatanyabikorwa',
      'document': 'Inyandiko'
    }
  };

  // Language selector functionality
document.addEventListener('DOMContentLoaded', function() {
    const languageSelector = document.querySelector('.fb-language-selector');
    const selectedLanguage = languageSelector.querySelector('.selected-language');
    const languageDropdown = languageSelector.querySelector('.language-dropdown');
    
    // Toggle dropdown
    selectedLanguage.addEventListener('click', function(e) {
      e.stopPropagation();
      languageDropdown.classList.toggle('show');
    });
    
    // Close when clicking outside
document.addEventListener('click', function() {
      languageDropdown.classList.remove('show');
    });
    
    // Language selection
document.querySelectorAll('.language-option').forEach(option => {
      option.addEventListener('click', function() {
        const lang = this.dataset.lang;
        translateNavbar(lang);
        selectedLanguage.querySelector('span').textContent = lang.toUpperCase();
        languageDropdown.classList.remove('show');
        localStorage.setItem('preferredLang', lang);
      });
    });
    
    // Load preferred language if set
    const savedLang = localStorage.getItem('preferredLang');
    if (savedLang) {
      translateNavbar(savedLang);
      selectedLanguage.querySelector('span').textContent = savedLang.toUpperCase();
    }
  });
function translateNavbar(lang) {
    document.querySelectorAll('[data-translate]').forEach(el => {
      const key = el.dataset.translate;
      if (translations[lang] && translations[lang][key]) {
        el.textContent = translations[lang][key];
      }
    });
  }

function toggleMenu() {
    const navLinks = document.getElementById("navLinks");
    navLinks.classList.toggle("active");
  }

function toggleDropdown() {
    const dropdown = document.getElementById("dropdownContent");
    dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
  }

  // Close the dropdown if clicked outside
  window.onclick = function(event) {
    if (!event.target.matches('.dropdown-button')) {
      const dropdowns = document.getElementsByClassName("dropdown-content");
      for (let i = 0; i < dropdowns.length; i++) {
        dropdowns[i].style.display = "none";
      }
    }
  };
window.addEventListener('scroll', function() {
    var navbar = document.getElementById('navbar3r');
    if (window.scrollY > 50) {
      navbar.classList.add('navbar-scrolled');
    } else {
      navbar.classList.remove('navbar-scrolled');
    }
  });

document.getElementById('partnerForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const subject = document.getElementById('subject').value.trim();

    if (!name || !email) {
      alert("Please fill out all required fields.");
      return;
    }

    console.log("Form submitted:", { name, email, subject });
    alert("Thank you for reaching out! We'll get back to you soon.");
    this.reset();
  });
// Chat bot functionality
const chatBot = {
currentQuestion: 0,
userAnswers: {},
questions: [
  {
    question: "Hello! How can we help you today?",
    options: [
      "I want to learn about your projects",
      "I need contact information",
      "I want to make a donation",
      "Other question"
    ],
    key: "purpose"
  },
  {
    question: "Which type of project are you interested in?",
    options: [
      "Education initiatives",
      "Healthcare programs",
      "Community empowerment",
      "All projects"
    ],
    key: "project_type",
    showIf: (answers) => answers.purpose === "I want to learn about your projects"
  },
  {
    question: "How would you like to contact us?",
    options: [
      "Email",
      "Phone call",
      "Visit our office",
      "Social media"
    ],
    key: "contact_method",
    showIf: (answers) => answers.purpose === "I need contact information"
  },
  {
    question: "What donation method would you prefer?",
    options: [
      "Online payment",
      "Bank transfer",
      "Mobile money",
      "In-person donation"
    ],
    key: "donation_method",
    showIf: (answers) => answers.purpose === "I want to make a donation"
  },
  {
    question: "Please describe your question and we'll get back to you shortly.",
    options: [],
    key: "other_question",
    showIf: (answers) => answers.purpose === "Other question",
    inputField: true
  }
],

getNextQuestion: function(answers) {
  for (let i = this.currentQuestion + 1; i < this.questions.length; i++) {
    const question = this.questions[i];
    if (!question.showIf || question.showIf(answers)) {
      return question;
    }
  }
  return null;
}
};

// Chat UI functionality
let isChatOpen = false;

function toggleChatBox() {
const chatBox = document.getElementById('chatBox');
const chatNotification = document.getElementById('chatNotification');

isChatOpen = !isChatOpen;
chatBox.style.display = isChatOpen ? 'flex' : 'none';
chatNotification.style.display = 'none';

if (isChatOpen && document.getElementById('chatMessages').children.length === 0) {
  startChat();
}
}
function startChat() {
chatBot.currentQuestion = 0;
chatBot.userAnswers = {};
displayQuestion(chatBot.questions[0]);
}

function displayQuestion(question) {
const chatMessages = document.getElementById('chatMessages');
const quickReplyOptions = document.getElementById('quickReplyOptions');
const textInputArea = document.querySelector('.text-input-area');

// Add bot message
addMessage(question.question, 'bot');

// Show typing indicator
const typingIndicator = document.createElement('div');
typingIndicator.className = 'typing-indicator';
typingIndicator.innerHTML = '<span></span><span></span><span></span>';
chatMessages.appendChild(typingIndicator);

// Scroll to bottom
chatMessages.scrollTop = chatMessages.scrollHeight;

// Clear previous options
quickReplyOptions.innerHTML = '';

// After a short delay, show options
setTimeout(() => {
  // Remove typing indicator
  if (chatMessages.lastChild === typingIndicator) {
    chatMessages.removeChild(typingIndicator);
  }
  
  if (question.options.length > 0) {
    // Add quick reply buttons
    question.options.forEach(option => {
      const button = document.createElement('button');
      button.className = 'quick-reply-btn';
      button.textContent = option;
      button.onclick = () => selectOption(option, question.key);
      quickReplyOptions.appendChild(button);
    });
    
    textInputArea.style.display = 'none';
    quickReplyOptions.style.display = 'flex';
  } else {
    // Show text input for open-ended questions
    quickReplyOptions.style.display = 'none';
    textInputArea.style.display = 'flex';
    document.getElementById('chatInput').focus();
  }
  
  // Scroll to bottom again after options are added
  chatMessages.scrollTop = chatMessages.scrollHeight;
}, 1000);
}

function selectOption(option, key) {
// Store user answer
chatBot.userAnswers[key] = option;

// Add user message to chat
addMessage(option, 'user');

// Get next question
const nextQuestion = chatBot.getNextQuestion(chatBot.userAnswers);

if (nextQuestion) {
  chatBot.currentQuestion = chatBot.questions.indexOf(nextQuestion);
  setTimeout(() => displayQuestion(nextQuestion), 500);
} else {
  // End of conversation
  setTimeout(() => {
    addMessage("Thank you for chatting with us! We'll get back to you soon.", 'bot');
    document.getElementById('quickReplyOptions').innerHTML = '';
    document.querySelector('.text-input-area').style.display = 'none';
    
    // Here you would typically send the conversation to your backend
    console.log("Conversation summary:", chatBot.userAnswers);
  }, 500);
}
}

function sendMessage() {
const input = document.getElementById('chatInput');
const message = input.value.trim();

if (message) {
  const currentQuestion = chatBot.questions[chatBot.currentQuestion];
  selectOption(message, currentQuestion.key);
  input.value = '';
}
}

function addMessage(text, sender) {
const chatMessages = document.getElementById('chatMessages');
const messageDiv = document.createElement('div');
messageDiv.className = `message ${sender}-message`;
messageDiv.textContent = text;
chatMessages.appendChild(messageDiv);
chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Allow pressing Enter to send message
document.getElementById('chatInput')?.addEventListener('keypress', function(e) {
if (e.key === 'Enter') {
  sendMessage();
}
});

// Show notification badge when new message arrives (example)
setTimeout(() => {
if (!isChatOpen) {
  document.getElementById('chatNotification').style.display = 'flex';
}
}, 10000);
  // Toggle About Us dropdown
function toggleAboutDropdown() {
const dropdown = document.getElementById("aboutDropdown");
dropdown.classList.toggle("active");

// Close other dropdowns if open
document.querySelectorAll('.dropdown').forEach(otherDropdown => {
  if (otherDropdown !== dropdown && otherDropdown.classList.contains('active')) {
    otherDropdown.classList.remove('active');
  }
});
}

// Close dropdown when clicking outside
document.addEventListener('click', function(event) {
if (!event.target.closest('.dropdown')) {
  document.querySelectorAll('.dropdown').forEach(dropdown => {
    dropdown.classList.remove('active');
  });
}
});

// Close dropdown when clicking on a dropdown item
document.querySelectorAll('.dropdown-content a').forEach(item => {
item.addEventListener('click', () => {
  document.querySelectorAll('.dropdown').forEach(dropdown => {
    dropdown.classList.remove('active');
  });
});
});