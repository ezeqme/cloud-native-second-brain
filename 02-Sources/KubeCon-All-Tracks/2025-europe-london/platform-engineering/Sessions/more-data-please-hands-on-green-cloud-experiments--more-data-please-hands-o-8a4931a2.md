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
themes: ["Platform Engineering", "Storage Data", "Sustainability"]
speakers: ["Leonard Pahlke", "BWI GmbH", "Antonio Di Turi", "Data Reply"]
sched_url: https://kccnceu2025.sched.com/event/1tx9z/more-data-please-hands-on-green-cloud-experiments-leonard-pahlke-bwi-gmbh-antonio-di-turi-data-reply
youtube_search_url: https://www.youtube.com/results?search_query=More+Data+Please%3A+Hands+on+Green+Cloud+Experiments+CNCF+KubeCon+2025
slides: []
status: parsed
---

# More Data Please: Hands on Green Cloud Experiments - Leonard Pahlke, BWI GmbH & Antonio Di Turi, Data Reply

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Storage Data]], [[Sustainability]]
- País/cidade: United Kingdom / London
- Speakers: Leonard Pahlke, BWI GmbH, Antonio Di Turi, Data Reply
- Schedule: https://kccnceu2025.sched.com/event/1tx9z/more-data-please-hands-on-green-cloud-experiments-leonard-pahlke-bwi-gmbh-antonio-di-turi-data-reply
- Busca YouTube: https://www.youtube.com/results?search_query=More+Data+Please%3A+Hands+on+Green+Cloud+Experiments+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre More Data Please: Hands on Green Cloud Experiments.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx9z/more-data-please-hands-on-green-cloud-experiments-leonard-pahlke-bwi-gmbh-antonio-di-turi-data-reply
- YouTube search: https://www.youtube.com/results?search_query=More+Data+Please%3A+Hands+on+Green+Cloud+Experiments+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4OdYWliYpPg
- YouTube title: More Data Please: Hands on Green Cloud Experiments - Leonard Pahlke & Antonio Di Turi
- Match score: 0.84
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/more-data-please-hands-on-green-cloud-experiments/4OdYWliYpPg.txt
- Transcript chars: 23005
- Keywords: basically, energy, environment, entire, hardware, interesting, numbers, actually, measure, software, stress, measurements, always, access, consumption, microser, bigger, already

### Resumo baseado na transcript

Um yeah like my name is Antonio here with me uh we have Leo and today we'll have our talk uh more data please ends on green cloud experiments. So yeah like in this 20 years we uh recently had the 10 years anniversary of Kubernetes. It means that we buy hardware that we just as Antonio said look at servers not for the first time but uh sort of um getting into bare metal thinking about okay how does storage look like? how different types of stoages do you have in not just like an abstracted kind of way from cloud providers where you have different storage tiers and whatever it is but actually the bare metal part um and this sort of led to building um Um this was like primarily also in a way like self-driven a learning experience getting into this entire rabbit hole of other technology um which is also very interesting um probably also like in other environments. But we chose Gfandra to um basically get all the different metrics energy metrics essentially about our workloads and then we do like some analysis later.

### Excerpt da transcript

Hi everybody. Um yeah like my name is Antonio here with me uh we have Leo and today we'll have our talk uh more data please ends on green cloud experiments. Um so yeah like actually I've looked this up. It's been yeah more or less 20 years the term cloud has been out. So yeah like in this 20 years we uh recently had the 10 years anniversary of Kubernetes. So it's a very established industry and we all know why uh the dream of the cloud has become true. So we have scalability so res a lot of resources on demand agility so the faster dev um for for the cycles and like there are a lot of abstraction right like a lot of complexity that has been made simple. On the other hand we have some hidden costs. So we have energy demand that we rarely measure and also we have infrastructures detachment. So actually the first time I saw a server was like this year and it was like he had this noisy big machine that takes a lot of heat and it's like I never seen one right like I never had to see one. I don't know how how many people can relate but it was like quite impressive and yeah like we we are getting towards a a world in which you're more oriented to application development and a little bit loss of technical knowledge to their deepest stack.

So on on the other side we also have software that gets bigger in a way right like hardware has never been easier to provision. So just a click away we can have more compute, more nodes and our software just gets bigger and bigger like I I remember like we had some discussion because we ended up having docker files or docker images that have 2 gigabytes in size and like maybe this was not possible like I don't know 20 30 years ago and that's maybe because we have memory bloat so we don't care what uh allocation we do of the memory we have execution bloat or simply we have environmental blind spot. So how did we get there, right? Um I mean it's it's hard to answer probably the reason are different but probably also abundant compute as an answer. So why optimize when it just take one second to put one more node on like a bigger one. So it's just cheaper to go this way or like also the fast market um has pushed us to develop more and more features, right? Like that's what we call feature creep. And also there are so many layers that we if we have to deep dive maybe we just not able to like because we don't understand a lot of layers that are deep deep behind.

So that's why we wanted to to set this talk and yeah I'm going to give t
