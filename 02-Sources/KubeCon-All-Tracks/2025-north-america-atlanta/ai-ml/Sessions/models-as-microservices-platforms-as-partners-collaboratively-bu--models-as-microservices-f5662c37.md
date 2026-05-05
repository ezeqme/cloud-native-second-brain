---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "AI + ML"
themes: ["AI ML", "Platform Engineering"]
speakers: ["Stephanie Pavlick", "Hinge"]
sched_url: https://kccncna2025.sched.com/event/27FYz/models-as-microservices-platforms-as-partners-collaboratively-building-ml-infra-at-hinge-stephanie-pavlick-hinge
youtube_search_url: https://www.youtube.com/results?search_query=Models+as+Microservices%2C+Platforms+as+Partners%3A+Collaboratively+Building+ML+Infra+at+Hinge+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Models as Microservices, Platforms as Partners: Collaboratively Building ML Infra at Hinge - Stephanie Pavlick, Hinge

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Platform Engineering]]
- País/cidade: United States / Atlanta
- Speakers: Stephanie Pavlick, Hinge
- Schedule: https://kccncna2025.sched.com/event/27FYz/models-as-microservices-platforms-as-partners-collaboratively-building-ml-infra-at-hinge-stephanie-pavlick-hinge
- Busca YouTube: https://www.youtube.com/results?search_query=Models+as+Microservices%2C+Platforms+as+Partners%3A+Collaboratively+Building+ML+Infra+at+Hinge+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Models as Microservices, Platforms as Partners: Collaboratively Building ML Infra at Hinge.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FYz/models-as-microservices-platforms-as-partners-collaboratively-building-ml-infra-at-hinge-stephanie-pavlick-hinge
- YouTube search: https://www.youtube.com/results?search_query=Models+as+Microservices%2C+Platforms+as+Partners%3A+Collaboratively+Building+ML+Infra+at+Hinge+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6H88ez69VmQ
- YouTube title: Models as Microservices, Platforms as Partners: Collaboratively Building ML Inf... Stephanie Pavlick
- Match score: 0.965
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/models-as-microservices-platforms-as-partners-collaboratively-building/6H88ez69VmQ.txt
- Transcript chars: 25056
- Keywords: platform, serving, actually, models, online, engineers, little, developing, training, specific, pieces, observability, important, better, bricks, awesome, custom, mlflow

### Resumo baseado na transcript

And today I'm really excited to talk to all of you a little bit about how we're approaching developing an ML platform from the ground up at Hinge. And I'm going to talk a bit about this, not just from a technical perspective, but also from kind of a perspective of how we've approached building the platform over time. So, just to give you an overview of AI at Hinge, what our org looks like, and some of the different problems that we're solving using AI, um, we have a few different areas of focus. And as we've grown, as we scaled, you know, something like that works when you're smaller, just coming up. Um, but as you scale, you start to find that you're kind of reinventing the wheel every time you want to productize a model. So as again as you scale you can take some of that load off of engineers as well as we were finding that there was a bottleneck in our time to production for models.

### Excerpt da transcript

All right, awesome. Hello everyone. I hope everyone's having an awesome CubeCon so far. I know I am. And today I'm really excited to talk to all of you a little bit about how we're approaching developing an ML platform from the ground up at Hinge. And I'm going to talk a bit about this, not just from a technical perspective, but also from kind of a perspective of how we've approached building the platform over time. because I'm sure a lot of you are familiar. Platform engineering is really both a science and an art. Um, so before getting into things, just want to introduce myself a little bit. Hello everyone. I'm Stephanie Pavick. I'm a machine learning platform engineer at Hinge. And while at Hinge, I've been working on a wide array of different pieces of our platform, but I'm mostly f focused on the model serving side as well as implementing a lot of our observability stack. And just in my free time, I really really love biking. So if you're into biking, I'd love to talk to you about it or if you're into platform engineering.

Um, so just to give a little bit of an overview of some of the topics I'm going to be talking about today. First I'm going to start with an overview of AI at Hinge, how some of our different um products that we're developing. Then I'm going to go into our platform, how it's evolved over time, and then I'm going to dive a little bit deeper into our serving platform, and then finally end with some of the lessons we've learned in the process of building this out. So, just to give you an overview of AI at Hinge, what our org looks like, and some of the different problems that we're solving using AI, um, we have a few different areas of focus. So, you might guess that AI is really important to powering our matching algorithm that's able to show users different people that they'll be compatible with. So this work lives under our dating outcomes team, but that team does a lot of other work as well. We have a lot of really cool features that are powered by AI that help you make your profile even better, help you better able to make your perfect match.

Some of these are, for example, um prompt feedback. So, we have a really cool feature that tells you, it will prompt you if you can better add some detail to your prompt to be able to spark conversation better. We also have um a model called top photo that's able to when in other people's feed display the photo out of your photos that will help um better get you a match. We also have the tru
