# Function to collect responses
def get_responses():
    questions = [
        # Active Learner (1-10)
        "1. I enjoy trying out new activities and experiences.",
        "2. I often act on impulse rather than plan ahead.",
        "3. I feel energized when working with a team or in a group.",
        "4. I prefer to get involved in tasks right away without much preparation.",
        "5. I find it easy to adapt to sudden changes or unexpected situations.",
        "6. I enjoy brainstorming sessions where I can contribute ideas freely.",
        "7. I prefer to learn by doing rather than by reading or listening.",
        "8. I find theoretical discussions less engaging than hands-on practice.",
        "9. I am comfortable with taking risks and trying out new approaches.",
        "10. I often start projects without fully planning them in advance.",

        # Reflective Learner (11-20)
        "11. I prefer to think things through before taking action.",
        "12. I like to observe and listen before contributing to a group discussion.",
        "13. I tend to reflect on past experiences before making decisions.",
        "14. I enjoy reviewing information and considering different perspectives before forming an opinion.",
        "15. I prefer to have time to work alone and process my thoughts.",
        "16. I often write down my thoughts or keep a journal to reflect on what I’ve learned.",
        "17. I need to understand the reasoning behind actions before I feel comfortable proceeding.",
        "18. I take my time when making important decisions to consider all angles.",
        "19. I enjoy reviewing notes or reading over materials after a lesson to reinforce my learning.",
        "20. I find it useful to evaluate my performance after completing a task or project.",

        # Theoretical Learner (21-30)
        "21. I enjoy understanding the principles and theories behind a concept.",
        "22. I prefer structured learning where I can analyze information step-by-step.",
        "23. I like to organize information into logical sequences or systems.",
        "24. I enjoy reading and researching topics in depth to understand them fully.",
        "25. I prefer to rely on data, facts, and evidence rather than intuition.",
        "26. I enjoy solving complex problems that require logical thinking.",
        "27. I feel more confident when I can apply established methods and principles to solve a problem.",
        "28. I enjoy analyzing abstract concepts and making connections between them.",
        "29. I prefer to learn by studying established theories rather than experimenting.",
        "30. I feel more comfortable with ideas that have been proven and tested.",

        # Practical Learner (31-40)
        "31. I enjoy applying what I’ve learned to real-world situations.",
        "32. I prefer learning activities that have a clear, practical purpose.",
        "33. I feel more motivated when I can see the immediate benefits of a task or skill.",
        "34. I prefer to focus on techniques and skills that are useful in everyday life or work.",
        "35. I like to test new ideas or theories by putting them into practice.",
        "36. I enjoy learning through trial and error in real-life settings.",
        "37. I prefer tasks where I can produce something tangible or measurable.",
        "38. I find it easier to understand concepts when they are presented with examples from real life.",
        "39. I often think about how I can use what I’m learning in my personal or professional life.",
        "40. I get frustrated with abstract ideas that don’t seem to have practical applications.",

        # Combination Learner (41-50)
        "41. I like to experiment with new ideas, but I also take time to think about how they worked afterward.",
        "42. I prefer to balance theory and practice, using a mix of research and hands-on application.",
        "43. I enjoy working with a group, but I also need time to reflect on what I’ve learned.",
        "44. I can adapt my learning style depending on the situation or task at hand.",
        "45. I enjoy breaking down complex theories, but I like to see how they work in real life.",
        "46. I feel motivated when I understand both the ‘why’ and the ‘how’ of a task.",
        "47. I like to collaborate with others but need time to evaluate my contributions afterward.",
        "48. I often combine my instincts with logic when solving a problem.",
        "49. I enjoy learning from both my successes and my mistakes.",
        "50. I feel confident when I can see both the big picture and the practical steps involved."
    ]

    return questions


# Function to calculate scores
def calculate_scores(responses):
    scores = {
        "Active": sum(responses[0:10]),
        "Reflective": sum(responses[10:20]),
        "Theoretical": sum(responses[20:30]),
        "Practical": sum(responses[30:40]),
        "Combination": sum(responses[40:50])
    }
    return scores

