---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability", "Community"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/oss-supply-chain---are-prometheu/
youtube_url: https://www.youtube.com/watch?v=UZ-MxQpaogY
youtube_search_url: https://www.youtube.com/results?search_query=OSS+Supply+Chain+-+Are+Prometheus+Exporters+the+Weak+Link%3F+PromCon+2022
video_match_score: 1.003
status: video-found
---

# OSS Supply Chain - Are Prometheus Exporters the Weak Link?

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]], [[Community]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/oss-supply-chain---are-prometheu/
- YouTube: https://www.youtube.com/watch?v=UZ-MxQpaogY

## Resumo

Speaker(s): David de Torres Huerta The supply chain in open source projects has become the elephant in the room of every ecosystem, and Prometheus is no exception. However, Prometheus is not just one project but a large open-source ecosystem of projects: the exporters. And the majority of these exporters are beyond the scope of the main Prometheus project and community.

## Abstract oficial

Speaker(s): David de Torres Huerta

The supply chain in open source projects has become the elephant in the room of every ecosystem, and Prometheus is no exception. However, Prometheus is not just one project but a large open-source ecosystem of projects: the exporters. And the majority of these exporters are beyond the scope of the main Prometheus project and community.

The reason for this is that few applications provide out-of-the-box Prometheus metrics, and we can see how the original idea of allowing the open-source community to create Prometheus exporters at will has resulted in a heterogeneous ecosystem in which:


You can find more than one exporter for the same application
Configurations are not homogeneous
Prometheus best practices and conventions are not always followed


Most crucially, the majority of them are independent open source projects maintained by independent open source contributors. They may or may not continue with the project with the degree of security and performance necessary for production environments in the future.

In this talk, we will explore the potential risk of exporters in the Prometheus supply chain and some ideas of how to improve our ecosystem.

## Links

- Página oficial: https://promcon.io/2022-munich/talks/oss-supply-chain---are-prometheu/
- YouTube: https://www.youtube.com/watch?v=UZ-MxQpaogY
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UZ-MxQpaogY
- YouTube title: PromCon EU 2022: OSS Supply Chain - Are Prometheus Exporters the Weak Link?
- Match score: 1.003
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/oss-supply-chain-are-prometheus-exporters-the-weak-link/UZ-MxQpaogY.txt
- Transcript chars: 18289
- Keywords: source, exporter, prometheus, exporters, company, companies, communities, making, another, metrics, applications, started, working, projects, happened, contribute, supply, talking

### Resumo baseado na transcript

[Music] foreign [Music] so I'm going to be emceeing for the rest of the day because would be nice to have an introduction I'm Julius one of the Prometheus co-founders and the next talk is going to be David de Torres from systic about OSS supply chain I guess security right so looking forward to that thank you [Applause] well open source Supply change there are a lot of ways to talk about this and I think I chose the one that is not usually done so expect this to

### Excerpt da transcript

[Music] foreign [Music] so I'm going to be emceeing for the rest of the day because would be nice to have an introduction I'm Julius one of the Prometheus co-founders and the next talk is going to be David de Torres from systic about OSS supply chain I guess security right so looking forward to that thank you [Applause] well open source Supply change there are a lot of ways to talk about this and I think I chose the one that is not usually done so expect this to be the most different talk that you will see here in the prom con wish me luck uh first I need to introduce myself I Am David de Torres I am a believer in the open source sometimes idealist I studied science computer science and anthropology I have a daughter I'm allergic to cats I am a contributor and one of the founders of the pronka.io open source project here with my colleagues and right now I'm working at sezick at as an engineering manager but why I'm telling you all this personal trivia because if we want to talk about open source Supply chains we need to talk about communities but communities is nothing else that people and there are people with a common culture and doing things together and if we want to talk about communities there are people that has been studying communities all around the world for more than 100 years on their anthropology so let's use in this talk some of their findings to try to find something deeper in our open source communities this is one of the anthropologists that I like most it is Eric wolf Eric wolf did something strange like that I'm doing right now today he while in the anthropology in the 80s they were talking about big words like structuralism or functionalism or things like this like we are talking now about open source projects and communities and Supply chains then he took a different approach and he focused on people and he used something called microstories and he told the story personal stories of the people to describe how communities behave and how many communities where interacting each other so let's make an experiment Let's Talk About Me Chris stories in the open source world and I will tell mine this is the one and I know most but it can be any of you because most probably mine is no different from yours I want to start three years ago I was in a company and I was working in the industrial monitoring and then in one of my home local meetups I heard about Prometheus and then I said wow this seems amazing and I started to install it and test it
