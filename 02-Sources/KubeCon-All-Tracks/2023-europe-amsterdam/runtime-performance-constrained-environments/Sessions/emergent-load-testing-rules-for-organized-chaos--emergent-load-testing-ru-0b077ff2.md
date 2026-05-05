---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Runtime Performance + Constrained Environments"
themes: ["AI ML", "Runtime Containers", "SRE Reliability"]
speakers: ["Nicole van der Hoeven", "Grafana Labs"]
sched_url: https://kccnceu2023.sched.com/event/1HyYH/emergent-load-testing-rules-for-organized-chaos-nicole-van-der-hoeven-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Emergent+Load+Testing%3A+Rules+for+Organized+Chaos+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Emergent Load Testing: Rules for Organized Chaos - Nicole van der Hoeven, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Runtime Performance + Constrained Environments]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Nicole van der Hoeven, Grafana Labs
- Schedule: https://kccnceu2023.sched.com/event/1HyYH/emergent-load-testing-rules-for-organized-chaos-nicole-van-der-hoeven-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Emergent+Load+Testing%3A+Rules+for+Organized+Chaos+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Emergent Load Testing: Rules for Organized Chaos.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyYH/emergent-load-testing-rules-for-organized-chaos-nicole-van-der-hoeven-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Emergent+Load+Testing%3A+Rules+for+Organized+Chaos+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YhHX2ULmnOo
- YouTube title: Emergent Load Testing: Rules for Organized Chaos - Nicole van der Hoeven, Grafana Labs
- Match score: 0.809
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/emergent-load-testing-rules-for-organized-chaos/YhHX2ULmnOo.txt
- Transcript chars: 31529
- Keywords: emergence, testing, actually, emergent, application, affordances, already, evolution, imperative, browser, generative, important, actual, sometimes, affordance, interact, though, little

### Resumo baseado na transcript

I'm Nicole vonderhoven and I'm not actually touched by Blood I'm Dutch by nationality though and residence which is what counts I'm a developer Advocate at grafana labs and today I'm going to talk about emergent load testing one of my favorite topics I have been a performance tester for over 12 years and so today I'm going to be telling you what emergence is and then I'm going to raise some questions and maybe have a few answers for how we could apply that to our testing especially load equals true browser tests in k6 can give metrics that are that add to what you can get with a protocol level test if you're only testing on the protocol level you're missing out on the actual user experience of how long does something take

### Excerpt da transcript

I'm Nicole vonderhoven and I'm not actually touched by Blood I'm Dutch by nationality though and residence which is what counts I'm a developer Advocate at grafana labs and today I'm going to talk about emergent load testing one of my favorite topics I have been a performance tester for over 12 years and so today I'm going to be telling you what emergence is and then I'm going to raise some questions and maybe have a few answers for how we could apply that to our testing especially load testing I say maybe because while I do have code for some of these things it's always a bit difficult with a mixed crowd so consider this presentation a little bit more conceptual it's more of a testing approach than a fully fleshed out framework because I don't believe that many of those can be applied to everyone anyway so this is my definition of emergence emergence in general is the evolution of a whole Beyond its parts in unexpected ways we're going to go over this and we're going to have examples but in general um it's called an evolution because it is something that is iterative we're familiar with this as Engineers I'm sure and it is it is also important to note that these changes come about after Generations it's not something that just happens we can't always plan for emergence but we can do a few things to cause it to occur so the whole refers to the entire system so this could be an actual like application or it could be nature which we'll see in the next Slide the parts refer to individuals or components within the system and then the changes that are happening here are going to be unexpected because just like nature things sometimes happen we can plan for things but other things that are unexpected always come up and we just need to as Engineers be able to cope with them so let's look at an example in nature this is such a cool picture it's not my picture and it's a really fascinating creatures because if you take an individual ant they have very simplistic brains they're they're insects they're driven to do certain things and that's it they're not really thinking about the philosophical implications of it and it's actually a bit misleading to think of an ant Queen because that word doesn't mean for ants what it does to us and queen the ants don't have leaders the ant Queen is just another ant with a different role and when we think of a queen we think of some sort of leader whether that's an actual leader or a political figurehead it's still some sort of lead
