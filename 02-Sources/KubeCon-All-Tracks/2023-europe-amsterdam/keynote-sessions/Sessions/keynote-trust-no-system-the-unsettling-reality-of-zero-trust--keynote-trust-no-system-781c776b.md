---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Keynote Sessions"
themes: ["Security"]
speakers: ["Frederick Kautz", "Steering Committee Member", "SPIFFE/SPIRE"]
sched_url: https://kccnceu2023.sched.com/event/1HyR4/keynote-trust-no-system-the-unsettling-reality-of-zero-trust-frederick-kautz-steering-committee-member-spiffespire
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Trust+No+System%3A+The+Unsettling+Reality+of+Zero+Trust+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Keynote: Trust No System: The Unsettling Reality of Zero Trust - Frederick Kautz, Steering Committee Member, SPIFFE/SPIRE

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Frederick Kautz, Steering Committee Member, SPIFFE/SPIRE
- Schedule: https://kccnceu2023.sched.com/event/1HyR4/keynote-trust-no-system-the-unsettling-reality-of-zero-trust-frederick-kautz-steering-committee-member-spiffespire
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Trust+No+System%3A+The+Unsettling+Reality+of+Zero+Trust+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Keynote: Trust No System: The Unsettling Reality of Zero Trust.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyR4/keynote-trust-no-system-the-unsettling-reality-of-zero-trust-frederick-kautz-steering-committee-member-spiffespire
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Trust+No+System%3A+The+Unsettling+Reality+of+Zero+Trust+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YcYFghB2hE8
- YouTube title: Keynote: Trust No System: The Unsettling Reality of Zero Trust - Frederick Kautz, SPIFFE/SPIRE
- Match score: 0.885
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/keynote-trust-no-system-the-unsettling-reality-of-zero-trust/YcYFghB2hE8.txt
- Transcript chars: 14791
- Keywords: particular, security, question, trying, systems, context, trusting, happens, relationship, little, decision, radius, trusted, implicit, software, coming, concept, information

### Resumo baseado na transcript

all right everyone good morning our next presenter is my fellow coacher Frederick kautz Frederick is a steering committee member of spiffy Inspire and today we'll join Fred as he pulls back the curtain on the unsettling truth of software security and invite you to reconsider your approach to trust in the cloud please welcome Frederick Couts [Music] [Applause] and so before we get before we jump into the topic first I want to thank everyone for for coming over like the community I think has been absolutely fantastic so

### Excerpt da transcript

all right everyone good morning our next presenter is my fellow coacher Frederick kautz Frederick is a steering committee member of spiffy Inspire and today we'll join Fred as he pulls back the curtain on the unsettling truth of software security and invite you to reconsider your approach to trust in the cloud please welcome Frederick Couts [Music] [Applause] and so before we get before we jump into the topic first I want to thank everyone for for coming over like the community I think has been absolutely fantastic so like that's one of the things that we really tried to focus here was like how do we bring a a container together that's safe that people can come in and participate so again thank you everyone for being here and for those who are not able to be here we definitely hope to see you in the future uh you're also part of our community even if you weren't able to make it so please don't don't feel left out so but let's jump into something to an interesting topic was one that I find interesting so when we talk about security we often have to ask like what is our goal with with security and very often we have this concept of we're trying to hit confidentiality uh by trying to keep somebody in the piece of information secret or integrity that's not been modified or availability which conveniently uh spells out CIA uh easy to remember um but this is like a classic like like the Renaissance of art where people's really started to think through these issues um but but the thing about it is that the thing we want to really focus on like why do we have security is not security for the sake of it it's always in the context of something and I want to really get down to the root of what that something is and it's really about establishing Trust and so like in the background of this image you can see a bank there like there's trust that's put in the banking system there's what happens when that trust in the banking system has been eroded you we've we've solved some events occur earlier this year that uh our indicators of of the damage that can occur when that when that trust is not there so the same thing happens with with us with companies or with individuals is what happens when that trust is eroded and part of the path is that when we want when we want to perform some tasks we want to perform something we we have to establish that trust like this little cat here that is climbing up and it's testing the branch to make sure the branch is not going to fall unde
