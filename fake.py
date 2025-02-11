import tkinter as tk
from tkinter import messagebox, scrolledtext
import re

class FakeReviewDetectorApp:
    def __init__(self, master):
        self.master = master
        master.title("Fake Review Detector")
        master.geometry("500x600")

        # Suspicious patterns and keywords
        self.suspicious_patterns = [
            r'amazing product',
            r'best ever',
            r'absolutely perfect',
            r'no complaints',
            r'five stars',
            r'must buy',
            r'100% recommend',
            r'changed my life'
        ]
        
        self.suspicious_keywords = [
            'fake', 'paid', 'sponsored', 'marketing', 
            'advertisement', 'promotion', 'influencer'
        ]

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Review input label and text area
        tk.Label(self.master, text="Enter Review:", font=('Arial', 12)).pack(pady=10)
        self.review_input = scrolledtext.ScrolledText(
            self.master, 
            height=10, 
            width=60, 
            wrap=tk.WORD, 
            font=('Arial', 10)
        )
        self.review_input.pack(padx=20, pady=10)

        # Detect Button
        detect_btn = tk.Button(
            self.master, 
            text="Detect Fake Review", 
            command=self.analyze_review,
            font=('Arial', 12),
            bg='lightblue'
        )
        detect_btn.pack(pady=10)

        # Result display area
        self.result_label = tk.Label(
            self.master, 
            text="", 
            font=('Arial', 12, 'bold'),
            wraplength=450
        )
        self.result_label.pack(pady=10)

        # Reasons display area
        self.reasons_text = scrolledtext.ScrolledText(
            self.master, 
            height=5, 
            width=60, 
            wrap=tk.WORD, 
            font=('Arial', 10),
            state='disabled'
        )
        self.reasons_text.pack(padx=20, pady=10)

    def detect_fake_review(self, review: str) -> dict:
        """Analyze review for potential fakeness"""
        review_lower = review.lower()
        fake_score = 0.0
        reasons = []
        
        # Check suspicious patterns
        pattern_matches = sum(
            1 for pattern in self.suspicious_patterns 
            if re.search(pattern, review_lower)
        )
        fake_score += pattern_matches * 0.2
        if pattern_matches > 0:
            reasons.append(f"Matched {pattern_matches} suspicious language patterns")
        
        # Check suspicious keywords
        keyword_matches = [
            keyword for keyword in self.suspicious_keywords 
            if keyword in review_lower
        ]
        fake_score += len(keyword_matches) * 0.3
        if keyword_matches:
            reasons.append(f"Found suspicious keywords: {', '.join(keyword_matches)}")
        
        # Length-based suspicion
        if len(review) < 50:
            fake_score += 0.4
            reasons.append("Review is unusually short")
        elif len(review) > 500:
            fake_score += 0.3
            reasons.append("Review is unusually long")
        
        # Normalize score
        fake_score = min(max(fake_score, 0), 1)
        
        return {
            "is_fake": fake_score > 0.5,
            "fake_probability": round(fake_score, 2),
            "reasons": reasons
        }

    def analyze_review(self):
        # Get review from input
        review = self.review_input.get("1.0", tk.END).strip()
        
        # Validate input
        if not review:
            messagebox.showwarning("Warning", "Please enter a review to analyze.")
            return
        
        # Detect fake review
        result = self.detect_fake_review(review)
        
        # Update result label
        if result['is_fake']:
            self.result_label.config(
                text=f"FAKE REVIEW DETECTED\nProbability: {result['fake_probability']}", 
                fg='red'
            )
        else:
            self.result_label.config(
                text=f"LIKELY GENUINE REVIEW\nProbability: {result['fake_probability']}", 
                fg='green'
            )
        
        # Update reasons
        self.reasons_text.config(state='normal')
        self.reasons_text.delete('1.0', tk.END)
        self.reasons_text.insert(tk.END, "\n".join(result['reasons']))
        self.reasons_text.config(state='disabled')

def main():
    root = tk.Tk()
    app = FakeReviewDetectorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()