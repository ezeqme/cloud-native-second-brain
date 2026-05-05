---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Business Value"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Alexander Simon Jones", "Canonical"]
sched_url: https://kccnceu2023.sched.com/event/1HyWF/building-a-kubernetes-experimentation-platform-with-openfeature-enabling-organisations-to-put-theory-into-practice-alexander-simon-jones-canonical
youtube_search_url: https://www.youtube.com/results?search_query=Building+a+Kubernetes+Experimentation+Platform+with+OpenFeature%3B+Enabling+Organisations+to+Put+Theory+Into+Practice+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Building a Kubernetes Experimentation Platform with OpenFeature; Enabling Organisations to Put Theory Into Practice - Alexander Simon Jones, Canonical

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Business Value]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Alexander Simon Jones, Canonical
- Schedule: https://kccnceu2023.sched.com/event/1HyWF/building-a-kubernetes-experimentation-platform-with-openfeature-enabling-organisations-to-put-theory-into-practice-alexander-simon-jones-canonical
- Busca YouTube: https://www.youtube.com/results?search_query=Building+a+Kubernetes+Experimentation+Platform+with+OpenFeature%3B+Enabling+Organisations+to+Put+Theory+Into+Practice+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Building a Kubernetes Experimentation Platform with OpenFeature; Enabling Organisations to Put Theory Into Practice.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyWF/building-a-kubernetes-experimentation-platform-with-openfeature-enabling-organisations-to-put-theory-into-practice-alexander-simon-jones-canonical
- YouTube search: https://www.youtube.com/results?search_query=Building+a+Kubernetes+Experimentation+Platform+with+OpenFeature%3B+Enabling+Organisations+to+Put+Theory+Into+Practice+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hlvoJhMx2HU
- YouTube title: Building a Kubernetes Experimentation Platform with OpenFeature; Enabling... - Alexander Jones
- Match score: 0.852
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/building-a-kubernetes-experimentation-platform-with-openfeature-enabli/hlvoJhMx2HU.txt
- Transcript chars: 24825
- Keywords: feature, actually, interesting, configuration, trying, testing, little, experiments, flagging, operator, effectively, across, thought, together, providers, certain, experiment, around

### Resumo baseado na transcript

so thank you very much for joining my name is Alex Jones and I'm going to be talking to you today a little bit about open feature just before we go into that I want to set the the scene of who I am and why I'm talking to you about this today uh I'm on the governing board of open future but I didn't start there I started as a contributor as often people do it was just something that I don't have anything to do in my work

### Excerpt da transcript

so thank you very much for joining my name is Alex Jones and I'm going to be talking to you today a little bit about open feature just before we go into that I want to set the the scene of who I am and why I'm talking to you about this today uh I'm on the governing board of open future but I didn't start there I started as a contributor as often people do it was just something that I don't have anything to do in my work with feature flagging but I find it interesting so aside from that I work as a engineering director at canonical and I also contribute to the cncf in a small way as well I would really encourage people to try and think about how you can contribute back to the cncf especially after the great talks we had from folks this morning and throughout the week so feature flagging it's an interesting thing so let's get into it and talk about why we should care about it what's open feature and even more interestingly what sort of experiments can we perform so this is kind of a looser gender of what we're going to do today we've got what is open feature how can I use it and how can I perform experiments and then maybe you'll have some ideas around here how you might integrate it into your own workflows and your own organizations so let's just quickly recap on what is a feature flag right I think many of us have a a view in our minds of yeah it's kind of a toggle thing that goes on and off and I really like the the words that a colleague of mine Pete Hodgson who also works with the open feature project put together um if you haven't seen modern Fowler's blog it's it's excellent but this effectively encapsulates how I would think of a feature flag right it's it's a way of being able to modify a system dynamically without causing any impact to the code of course you know in reality future lagging is pretty much changing the color of a website or you know a drop down a modal or maybe a new piece of functionality comes out so I think feature flagging has been sort of uh Typecast as something you see only in the web browser when the reality is anywhere you could put a feature flag so where are the gaps and why is something like open feature needed well the gaps of the first and foremost it's assumed to not be Cloud native right it's assumed to be something purely in in the web browser there isn't really a singular open source API right there aren't really well-known sdks and and free and open things that you can build feature flags with in a ubiquitous way th
