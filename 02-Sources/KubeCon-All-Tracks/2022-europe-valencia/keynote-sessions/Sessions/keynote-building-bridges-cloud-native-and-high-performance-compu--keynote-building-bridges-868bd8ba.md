---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Keynote Sessions"
themes: ["SRE Reliability"]
speakers: ["Ricardo Rocha", "Computing Engineer", "CERN"]
sched_url: https://kccnceu2022.sched.com/event/yuGH/keynote-building-bridges-cloud-native-and-high-performance-computing-ricardo-rocha-computing-engineer-cern
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Building+Bridges%3A+Cloud+Native+and+High+Performance+Computing+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Keynote: Building Bridges: Cloud Native and High Performance Computing - Ricardo Rocha, Computing Engineer, CERN

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[SRE Reliability]]
- País/cidade: Spain / Valencia
- Speakers: Ricardo Rocha, Computing Engineer, CERN
- Schedule: https://kccnceu2022.sched.com/event/yuGH/keynote-building-bridges-cloud-native-and-high-performance-computing-ricardo-rocha-computing-engineer-cern
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Building+Bridges%3A+Cloud+Native+and+High+Performance+Computing+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Keynote: Building Bridges: Cloud Native and High Performance Computing.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/yuGH/keynote-building-bridges-cloud-native-and-high-performance-computing-ricardo-rocha-computing-engineer-cern
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Building+Bridges%3A+Cloud+Native+and+High+Performance+Computing+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=M95AQi1wA_s
- YouTube title: Keynote: Building Bridges: Cloud Native and High Performance Computing - Ricardo Rocha
- Match score: 0.987
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/keynote-building-bridges-cloud-native-and-high-performance-computing/M95AQi1wA_s.txt
- Transcript chars: 17958
- Keywords: actually, workloads, talking, computing, resources, queues, performance, pretty, native, cluster, thousands, working, schedule, deployments, called, basically, everyone, earlier

### Resumo baseado na transcript

hello again i'm really happy to be here with everyone today i'll be talking about cloud native and high performance computing i think and the idea dave was just mentioning earlier about a batch but the batch working group that we're forming in the tag runtime of the toc one idea here is also to to talk about this today a bit i'll cover these topics so cloud native high performance computing i'm i'm a computing engineer at cern i will start with a cool picture that i took recently

### Excerpt da transcript

hello again i'm really happy to be here with everyone today i'll be talking about cloud native and high performance computing i think and the idea dave was just mentioning earlier about a batch but the batch working group that we're forming in the tag runtime of the toc one idea here is also to to talk about this today a bit i'll cover these topics so cloud native high performance computing i'm i'm a computing engineer at cern i will start with a cool picture that i took recently so i had a chance to go down to the atlas detector at cern this is the cavern 100 meters in the ground and i think this picture is quite nice because i like it and also because in the back you see the atlas detector and this is where we do the collisions we have this big particle accelerator where accelerate beams of protons we make them collide at precise points like this one and then we generate a lot of data out of these collisions and close to this detector on the ground we also have an online farm that will then take care of filtering the petabytes a second of data that we generate to something we can manage on the order of tens of gigabytes so in this farm it's actually a really interesting thing because back in when we started doing our kubernetes journey in 2016 just one year after this team reached out and asked us can we actually use kubernetes to modernize our systems as well so in 2017 we gave it a go we built a couple of thousand node cluster we saw a lot of issues trying to do what they wanted and what they want to do is to have thousands of services running at the same time when they have beam so that they can do the things i mentioned but when there is no beam and we have these periods where we replaced the beam with a new one they wanted to reuse the farm to do simulation which is pretty much batch workloads so they need to transition from one to the other very fast they need to schedule pods really fast at the time we couldn't do this we reached out to six scalability that we also heard jasmine talking about earlier and they actually fix these issues and today we can have a few thousand node clusters we can have uh 300 pods a second we just heard which matches their their needs and actually the next generation of this deployment will be based on kubernetes so i think it was a really nice way to start talking about cloud native and high performance by showing this this example so i'll also start talking about high performance computing with an uh an overview of wh
