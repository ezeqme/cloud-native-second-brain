---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Dillon TenBrink", "The Home Depot"]
sched_url: https://kccncna2025.sched.com/event/27FdX/flip-that-stack-renovating-edge-infrastructure-at-the-home-depot-dillon-tenbrink-the-home-depot
youtube_search_url: https://www.youtube.com/results?search_query=Flip+That+Stack%3A+Renovating+Edge+Infrastructure+at+the+Home+Depot+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Flip That Stack: Renovating Edge Infrastructure at the Home Depot - Dillon TenBrink, The Home Depot

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Atlanta
- Speakers: Dillon TenBrink, The Home Depot
- Schedule: https://kccncna2025.sched.com/event/27FdX/flip-that-stack-renovating-edge-infrastructure-at-the-home-depot-dillon-tenbrink-the-home-depot
- Busca YouTube: https://www.youtube.com/results?search_query=Flip+That+Stack%3A+Renovating+Edge+Infrastructure+at+the+Home+Depot+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Flip That Stack: Renovating Edge Infrastructure at the Home Depot.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FdX/flip-that-stack-renovating-edge-infrastructure-at-the-home-depot-dillon-tenbrink-the-home-depot
- YouTube search: https://www.youtube.com/results?search_query=Flip+That+Stack%3A+Renovating+Edge+Infrastructure+at+the+Home+Depot+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=p5Vca4BoiJw
- YouTube title: Flip That Stack: Renovating Edge Infrastructure at the Home Depot - Dillon TenBrink, The Home Depot
- Match score: 0.885
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/flip-that-stack-renovating-edge-infrastructure-at-the-home-depot/p5Vca4BoiJw.txt
- Transcript chars: 27349
- Keywords: platform, stores, retail, storage, needed, observability, environment, experience, created, another, around, transformation, software, developers, business, operating, within, talked

### Resumo baseado na transcript

And one of the things that I do both professionally and personally is I'm a builder. This is a picture from one of 17 homes that I've built in Austin as part of Habitat for Humanity work that we do in the community. That platform was built in a time where connectivity, reliability, uh, connectivity was on the end of really slow leased lines, maybe T1s, things that were not terribly reliable. And so the first lesson learned that I want you to take away is to understand your window of transformation. We could take a a real blue sky approach." And so we took and sketched up on a whiteboard our core set of design ideas. And I'm really happy to say that these design ideas which started out uh on a whiteboard in my office in 2017 still hold true today.

### Excerpt da transcript

Oh, you made it. You made it to the final day. You made it to the final hours. Give yourselves a round of applause. >> Yes. [applause] You survived. I survived, too. I'm here. We're all here together. Good morning. My name is Dylan Timberink. I'm a distinguished engineer at The Home Depot. Been with company a little over 14 years now. And one of the things that I do both professionally and personally is I'm a builder. I love to put things together. This is a picture from one of 17 homes that I've built in Austin as part of Habitat for Humanity work that we do in the community. Uh, but I also build a bunch of things. Some kit builder. I've built airplanes. I've built all sorts of things. And one of the things that I'm most proud of is the platform that we've built that runs our stores. And so today, I wanted to share with you lessons learned along the way of building the edge platform that powers the Home Depot retail experience out there today. We're going to give you some major points to consider if you are just starting down this road of building your own edge platform.

I hope you take away some of the lessons learned and you won't fall into some of the the pitfalls that we did along the way. And if you're an experienced edge builder or platform builder, maybe here's some additional things that you might relate to or consider as you continue to grow your platform. But first, I need to know, how many of you know about the Home Depot? It's my favorite question ever. Everybody loves Home Depot, right? Do I have any Canadians in the room? Excellent. Canadians. How about folks from Mexico? Oh my gosh, I love our Mexican stores. Thank you, Pablo. We are We are the world's largest home improvement retailer. We have over 2,300 locations spread across North America. We also have one of the largest retail websites in the world. And one of the challenges is is that we have to have all of these edge sites out there powering our retail experience. Also, another fun fact, I want to welcome those of you who are traveling as well. The Home Depot is based both founded and based here in Atlanta, Georgia.

So, if you've liked your trip out here to Atlanta, we welcome you. Um, hopefully you got over the cold weather earlier this week. Whenever you're starting to build something new, and in this case, we're going to relate it to building a home, just like the the the Habitat homes, you need to know the neighborhood that you're building in. And so, we had an existing edge pl
