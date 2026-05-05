---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Observability"
themes: ["AI ML", "Observability", "Kubernetes Core"]
speakers: ["Stevie Caldwell", "Fairwinds"]
sched_url: https://kccnceu2026.sched.com/event/2CVyr/the-hills-are-alive-with-the-sound-of-kubernetes-stevie-caldwell-fairwinds
youtube_search_url: https://www.youtube.com/results?search_query=The+Hills+Are+Alive+with+the+Sound+of+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# The Hills Are Alive with the Sound of Kubernetes - Stevie Caldwell, Fairwinds

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Stevie Caldwell, Fairwinds
- Schedule: https://kccnceu2026.sched.com/event/2CVyr/the-hills-are-alive-with-the-sound-of-kubernetes-stevie-caldwell-fairwinds
- Busca YouTube: https://www.youtube.com/results?search_query=The+Hills+Are+Alive+with+the+Sound+of+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre The Hills Are Alive with the Sound of Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVyr/the-hills-are-alive-with-the-sound-of-kubernetes-stevie-caldwell-fairwinds
- YouTube search: https://www.youtube.com/results?search_query=The+Hills+Are+Alive+with+the+Sound+of+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fzKp0YvS7Es
- YouTube title: The Hills Are Alive with the Sound of Kubernetes - Stevie Caldwell, Fairwinds
- Match score: 0.867
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/the-hills-are-alive-with-the-sound-of-kubernetes/fzKp0YvS7Es.txt
- Transcript chars: 18458
- Keywords: cluster, supercollider, little, sounds, controller, events, actually, visual, server, simple, pretty, deployment, sonification, information, happen, cocktail, created, already

### Resumo baseado na transcript

Um as long as I've been working in tech, one thing that I've noticed is that a lot of folks are also musicians on the side. I'm no exception, so I'm going to take this moment to uh shamelessly plug my side project, which is called And Then There Was One. Um as someone who makes music and works with Kubernetes, I wondered if there was a way to marry the two. So, that led me to thinking um you know, wouldn't it be cool if you could hear your Kubernetes cluster? I know for myself, I learn a lot better when I'm watching uh a tutorial when I have the video and the uh the audio and the visual in front of me rather than reading uh from a book alone. So, the architecture of uh of my um demo at a high level, uh we start off with a Kubernetes cluster.

### Excerpt da transcript

So, uh welcome to The Hills Are Alive with the Sound of Kubernetes. Uh this is a talk on sonification and observability. Let's see. So, um I am Stevie Caldwell. I am a senior tech lead for the SRE team at Fairwinds. Um as long as I've been working in tech, one thing that I've noticed is that a lot of folks are also musicians on the side. They have bands and and they make music and things like that. I'm no exception, so I'm going to take this moment to uh shamelessly plug my side project, which is called And Then There Was One. Uh you know, doing music is uh the primary motivator for me uh coming up with this talk. So, I make music in my home in my little uh homemade studio. It's essentially a desk. And then I upload them to streaming platforms like Spotify, Bandcamp, um and Apple Music. So, there's that. Uh so, as I said, I work for Fairwinds. Fairwinds is a managed services provider for Kubernetes. So, we build and maintain Kubernetes clusters for um a wide range of clients across a lot of different industries um to free up SRE, DevOps, and developer time uh from doing toil and drudgery things in Kubernetes and doing more exciting things like like something like this.

Uh so, let's see. So, in this talk, we are going to uh talk about what sonification is, the what and the why. Um I'm going to review my demo at uh a high level, the architecture of it um at a high level. And then I'm going to do a quick demo. Um so, let's get started. So, uh to start off with, sonification is the use of non-speech audio to convey information or perceptualized data. Simply put, it's using sound to represent data. Um this is a still taken from astronomy.com. It's an image of the sonification of a galaxy cluster. Uh you won't see anything this cool in my talk um because this is astronomy.com and I'm just Stevie. Uh and I have a day job. Um but I wanted to show this to you to show that although I'm doing this talk today is just like a fun little thing that I did, uh there are practical applications for this and there are very serious people and industries that do make use of sonification um in interesting ways. So, um I entered this talk or the idea for this talk a little backwards. Um as someone who makes music and works with Kubernetes, I wondered if there was a way to marry the two.

Um so, and to do something fun with it. So, that led me to thinking um you know, wouldn't it be cool if you could hear your Kubernetes cluster? And then, how would that be at all useful or, you
