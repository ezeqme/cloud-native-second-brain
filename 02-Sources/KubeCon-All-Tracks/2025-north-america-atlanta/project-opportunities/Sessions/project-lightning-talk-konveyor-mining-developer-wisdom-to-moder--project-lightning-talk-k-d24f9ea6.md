---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["AI ML"]
speakers: ["Jonah Sussman", "Developer / Approver"]
sched_url: https://kccncna2025.sched.com/event/28P5T/project-lightning-talk-konveyor-mining-developer-wisdom-to-modernize-legacy-apps-with-kai-jonah-sussman-developer-approver
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Konveyor%3A+Mining+Developer+Wisdom+to+Modernize+Legacy+Apps+with+Kai+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Konveyor: Mining Developer Wisdom to Modernize Legacy Apps with Kai - Jonah Sussman, Developer / Approver

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]]
- País/cidade: United States / Atlanta
- Speakers: Jonah Sussman, Developer / Approver
- Schedule: https://kccncna2025.sched.com/event/28P5T/project-lightning-talk-konveyor-mining-developer-wisdom-to-modernize-legacy-apps-with-kai-jonah-sussman-developer-approver
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Konveyor%3A+Mining+Developer+Wisdom+to+Modernize+Legacy+Apps+with+Kai+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Konveyor: Mining Developer Wisdom to Modernize Legacy Apps with Kai.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/28P5T/project-lightning-talk-konveyor-mining-developer-wisdom-to-modernize-legacy-apps-with-kai-jonah-sussman-developer-approver
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Konveyor%3A+Mining+Developer+Wisdom+to+Modernize+Legacy+Apps+with+Kai+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=urPCD5uMFk0
- YouTube title: Project Lightning Talk: Konveyor: Mining Developer Wisdom to Modernize Legacy Apps... Jonah Sussman
- Match score: 0.998
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-konveyor-mining-developer-wisdom-to-modernize-l/urPCD5uMFk0.txt
- Transcript chars: 5288
- Keywords: conveyor, applications, legacy, migration, static, analysis, agents, developer, accelerate, security, outdated, migrate, looking, modernize, migrations, technical, frameworks, vendors

### Resumo baseado na transcript

I'm going to be talking about Conveyor and how we are helping accelerate largecale migrations. If you're using like outdated frameworks, uh security risk, people are constantly trying to attack these outdated frameworks and maintenance costs. prior method or this prior pathway and so it can help accelerate the work that's being done and so you can see lm agent lm agent uh tool and then accept or reject and so every component of conveyor is designed to exponentially multiply your So if you want to get involved and learn more you can find our project on GitHub.

### Excerpt da transcript

Hi everybody, my name is Jonah Susman. I'm going to be talking about Conveyor and how we are helping accelerate largecale migrations. So first let's talk about the modernization problem. So there are real costs to having legacy code. So here are some examples. Um first off technical debt. Technical debt um slows down your processes. It makes uh things harder to work with. Uh security risks. If you're using like outdated frameworks, uh security risk, people are constantly trying to attack these outdated frameworks and maintenance costs. Um vendors will often have uh it will um it'll be more expensive if vendors, you know, you're using an outdated legacy framework. Plus, there's a skill gap where if you have like a really old framework that you're using, you might not be able to find somebody to fill the uh developer role. Okay, so let's say you've decided, hey, we've got these old apps and we're going to migrate something to more cloudnative. We're going to go away from like maybe Java 8 or something and we're going to go to something, you know, cool and fancy.

So you put in all this work, you migrate this app. It's great. But then let's say you have another app. Okay, so you kind of got to start over. You got to say, okay, well maybe we learned some things, but we kind of got to do all this grunt work again. Awesome. Great. What if you have another app? Okay, same thing. Well, what if you not don't have just three apps, you have 10 or hundreds. you know looking at this it makes me sad put a sad face on the presentation it makes me sad looking at this. So in conveyor we took a broad holistic view of migration experiences and we noticed some similar patterns across migrations and we categorized it into this conveyor unified experience. So often people would start off by surfacing information. They would analyze their applications and then understand what's inside them. So like uh we have a Java 8 app and we need to migrate to like Java 21. Next, we realized that people made decisions. They pri prioritized what needs to get done. Oh, this is a security vulnerability.

Oh, this is costing us a lot of money. We need to move away from that. Then they planned the work. They divided it up onto their developers and engineers. And then they actually perform the migration. And so we built conveyor specifically to accelerate this journey if you have lots of applications. So enter conveyor. So the core of conveyor is static analysis rules. So you can see it on the top
