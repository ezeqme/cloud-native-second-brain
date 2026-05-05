---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering"]
speakers: ["Majd Salman", "Jofre Mateu Matesanz", "Spotify"]
sched_url: https://kccnceu2025.sched.com/event/1tx9t/leveraging-internal-knowledge-building-aika-at-spotify-majd-salman-jofre-mateu-matesanz-spotify
youtube_search_url: https://www.youtube.com/results?search_query=Leveraging+Internal+Knowledge%3A+Building+AiKA+at+Spotify+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Leveraging Internal Knowledge: Building AiKA at Spotify - Majd Salman & Jofre Mateu Matesanz, Spotify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]]
- País/cidade: United Kingdom / London
- Speakers: Majd Salman, Jofre Mateu Matesanz, Spotify
- Schedule: https://kccnceu2025.sched.com/event/1tx9t/leveraging-internal-knowledge-building-aika-at-spotify-majd-salman-jofre-mateu-matesanz-spotify
- Busca YouTube: https://www.youtube.com/results?search_query=Leveraging+Internal+Knowledge%3A+Building+AiKA+at+Spotify+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Leveraging Internal Knowledge: Building AiKA at Spotify.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx9t/leveraging-internal-knowledge-building-aika-at-spotify-majd-salman-jofre-mateu-matesanz-spotify
- YouTube search: https://www.youtube.com/results?search_query=Leveraging+Internal+Knowledge%3A+Building+AiKA+at+Spotify+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FEy2lhe6CM8
- YouTube title: Leveraging Internal Knowledge: Building AiKA at Spotify - Majd Salman & Jofre Mateu Matesanz
- Match score: 0.846
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/leveraging-internal-knowledge-building-aika-at-spotify/FEy2lhe6CM8.txt
- Transcript chars: 21450
- Keywords: knowledge, information, spotify, documentation, platform, support, answer, question, questions, documents, sources, internal, context, retrieve, useful, answering, retrieval, search

### Resumo baseado na transcript

Uh so we're platform engineers in PDX, Spotify's uh platform developer experience department and we focus on building tools and systems uh that help make uh Spotify engineers more productive. Uh we both have been around eight years at Spotify working uh in different like corners of these internal platforms. With this scale it's not only difficult to keep all the information up to date. And they were often very costly to train from scratch or even to to fine-tune. These vectors are stored in a vector database and then when a when a user has a question that question uh or query is also converted using the same embedding model. Uh here we can see how we are asking about like a a general uh Python question and it's answering it without any problem.

### Excerpt da transcript

Nice to see so many of you here. Sorry to keep you waiting. I am Majid and this is Joffra. Uh so we're platform engineers in PDX, Spotify's uh platform developer experience department and we focus on building tools and systems uh that help make uh Spotify engineers more productive. Yes. Uh we both have been around eight years at Spotify working uh in different like corners of these internal platforms. Um during this time at the company we've seen a lot of growth and uh evol evolving. Um so that gave us like a good perspective of like uh the challenges that our engineers face on their daily life. Uh today we want to share with you how are we trying to address one of these productivity blockers with the help of AI. Uh let's take a look at how the problem looks like. So as a platform department we focus not only on measuring productivity uh we are also uh concerned about like what gets in the way of it. That's why in 2020 we started a quarterly engineering satisfaction survey uh we call it ENSAT to get data and trends on this productivity boosters and bloggers across all Spotify.

Since the very beginning and for every run, we've seen how issues uh with finding information or poor or missing documentation have been consistently in the top three. Uh what that means is that our engineers have to spend time uh looking across uh multiple systems to retrieve information. Let's look at how this recommendation looks like. So as a Spotify engineer, when you have uh some doubts, some issues, uh what do you do? First uh we have our internal documentation tech docs where we have more than 10,000 sites. With this scale it's not only difficult to keep all the information up to date. It's also find it it's also difficult to find the the right site that contains the information you're looking for. We also have code lots of it. Uh in GitHub we have readmis uh we have reference implementations and code examples that can save a lot of time for your daily tasks. um scattered around uh 22 different thousand uh 22,000 different repos. And when it comes to communication, we use Slack a lot. It's our main tool for internal support teams to teams.

So there we have a lot of our uh institutional troubleshooting knowledge. What happens with that is uh it's difficult to retrieve old answers that uh could answer your question. So teams have to balance a lot uh of their time between providing support and answering the same questions that get asked over and over again with their core work
