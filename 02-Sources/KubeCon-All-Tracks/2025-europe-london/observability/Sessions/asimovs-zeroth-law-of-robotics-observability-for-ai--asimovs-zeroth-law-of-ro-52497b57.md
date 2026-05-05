---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Observability"
themes: ["AI ML", "Observability"]
speakers: ["Nicole van der Hoeven", "Grafana Labs"]
sched_url: https://kccnceu2025.sched.com/event/1txEF/asimovs-zeroth-law-of-robotics-observability-for-ai-nicole-van-der-hoeven-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Asimov%27s+Zeroth+Law+of+Robotics%3A+Observability+for+AI+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Asimov's Zeroth Law of Robotics: Observability for AI - Nicole van der Hoeven, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]]
- País/cidade: United Kingdom / London
- Speakers: Nicole van der Hoeven, Grafana Labs
- Schedule: https://kccnceu2025.sched.com/event/1txEF/asimovs-zeroth-law-of-robotics-observability-for-ai-nicole-van-der-hoeven-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Asimov%27s+Zeroth+Law+of+Robotics%3A+Observability+for+AI+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Asimov's Zeroth Law of Robotics: Observability for AI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txEF/asimovs-zeroth-law-of-robotics-observability-for-ai-nicole-van-der-hoeven-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Asimov%27s+Zeroth+Law+of+Robotics%3A+Observability+for+AI+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=x6EKTCAWtn8
- YouTube title: Asimov's Zeroth Law of Robotics: Observability for AI - Nicole van der Hoeven, Grafana Labs
- Match score: 0.825
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/asimovs-zeroth-law-of-robotics-observability-for-ai/x6EKTCAWtn8.txt
- Transcript chars: 27217
- Keywords: testing, instructions, speedy, actually, selenium, wanted, graphana, evaluation, application, information, logs, potter, happened, specific, already, follow, followed, another

### Resumo baseado na transcript

I've also, if you play Pokemon Go, I always lure up the Pokéstops in my talk. I am a not just a senior developer advocate, but I'm also a performance engineer. Now, the problem is when you're in your spaceship and your robot is miles away, how do you know what happened? Costs can also increase quickly, especially if you're making a call to open AI, which is what I'm doing. Maybe maybe your application works really fast but you're impeded your performance is impeded by something further down which in this case would be the AI that you're that you're using and also latency matters especially in the specific case of an LLM a large So here are some specific AI specific telemetry signals that you might not have considered for metrics.

### Excerpt da transcript

Hi everyone. I'm Nicole Vanderhovven. I'm a senior developer advocate at Graphfana Labs. I've also, if you play Pokemon Go, I always lure up the Pokéstops in my talk. So have at it. I am a not just a senior developer advocate, but I'm also a performance engineer. Um, what I am not as a Python developer or an AI developer. I am a deep skeptic of AI, but I'm the kind of skeptic that wants to try it out for myself to see if my assumptions are founded. So, I'm approaching this with deep skepticism and hope. So, in 1941, radar had just become operational. the first jet aircraft took flight and Z3 which is the world's first programmable computer was created. So this was a time when digital machines were just beginning to think and somewhere in the world there was a biochemist and professor named Isaac Azimov who was already starting to think what if they do follow our instructions but it still somehow goes wrong. He's a skeptic after my own heart. So he came up with the three laws of robotics. Here are the three laws.

A robot may not injure a human being or through inaction allow a human being to come to harm. Number two, a robot must obey the orders given to it by humans. Number three, a robot must protect its own existence. And these three laws which are the first one is um is nonviolence. The second one is obedience and the third one is the self-preservation law. These are in order for a reason. The first always is going to be followed before the second and the second and the first will be followed before the third. And it's all very well reasoned out except when Azimov put forward these rules in his short story runaround which is part of a a series a book called Iroot which is excellent. This is actually what happened. This is Speedy. Speedy is a robot and a very intelligent robot. He and his owners were on Mercury where there were really um there was a it was very warm. That's that's saying putting it lightly. And Speedy was deployed to get the selenium deposits from a pool. They had identified the selenium, but his owners being humans could not stay long enough outside with outside their exo suits to collect the selenium themselves.

Now, the selenium was necessary for their fuel and they needed the selenium to go back home. So, they deployed Speedy, very reliable, very, very good robot following all of the instructions. And then Speedy just didn't return. Now, the problem is when you're in your spaceship and your robot is miles away, how do you know what
