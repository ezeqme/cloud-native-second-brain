---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Security"
themes: ["Security"]
speakers: ["Melissa Kilby", "Apple"]
sched_url: https://kccncna2023.sched.com/event/1R2mX/a-wind-of-change-for-threat-detection-melissa-kilby-apple
youtube_search_url: https://www.youtube.com/results?search_query=A+Wind+of+Change+for+Threat+Detection+CNCF+KubeCon+2023
slides: []
status: parsed
---

# A Wind of Change for Threat Detection - Melissa Kilby, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Chicago
- Speakers: Melissa Kilby, Apple
- Schedule: https://kccncna2023.sched.com/event/1R2mX/a-wind-of-change-for-threat-detection-melissa-kilby-apple
- Busca YouTube: https://www.youtube.com/results?search_query=A+Wind+of+Change+for+Threat+Detection+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre A Wind of Change for Threat Detection.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2mX/a-wind-of-change-for-threat-detection-melissa-kilby-apple
- YouTube search: https://www.youtube.com/results?search_query=A+Wind+of+Change+for+Threat+Detection+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1y1m9Vz93Yo
- YouTube title: A Wind of Change for Threat Detection - Melissa Kilby, Apple
- Match score: 0.867
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/a-wind-of-change-for-threat-detection/1y1m9Vz93Yo.txt
- Transcript chars: 28121
- Keywords: process, security, command, kernel, monitoring, attacks, counting, behavior, detection, production, events, information, sketch, container, application, environment, frequency, question

### Resumo baseado na transcript

hey I'm Melissa Kilby and I work in the services security engineering team at Apple which rolls right off the tongue when I first started in cyber security my initial Focus was on applying statistics AIML and big data to threat detection over time I realized that there were many gaps in terms of collecting the right data I then pivoted and started helping develop low-level Linux kernel monitoring tools and deployed them to production to gain firsthand experience of what is realistic and scalable earlier this year I became

### Excerpt da transcript

hey I'm Melissa Kilby and I work in the services security engineering team at Apple which rolls right off the tongue when I first started in cyber security my initial Focus was on applying statistics AIML and big data to threat detection over time I realized that there were many gaps in terms of collecting the right data I then pivoted and started helping develop low-level Linux kernel monitoring tools and deployed them to production to gain firsthand experience of what is realistic and scalable earlier this year I became a core maintainer of the Falco project today I will talk about how to use Falco with ebpf for runtime threat detection and more specifically focusing on how to use the right data effectively with more advanced analytics on the host itself including theories and Hands-On demos sometimes I'll go deep into details but I promise I always pull back out and I'll cover various aspects so hopefully everyone gets something out of it in case you didn't know a IML is pretty hot right now and then you look back at cyber security and threat detection and you think to yourself huh this is why we can't have nice things mainly because we don't have accurate training data sets still there must be a better way because the modern Cloud infrastructure attack surface is vast and the stakes are high attackers could gain unauthorized access to secrets and identities and subsequently steal customer data they could inject malicious code into the running applications or Worse attackers can infiltrate and temper with your build systems it's not 100% true that CIS calls or kernel events Never Lie the main message of the slide is that having a tool that hooks into the Linux kernel at system cause of Interest allows us to know what is going on with the running application including being able to detect if someone attacks the infrastructure for a wide range of attacks let's see how it's done in a quick hacking demo once upon a time there was a Jenkins server you know there won't be a happy ending suppose you found a vulnerability that allows you to get a shell back by exploiting the kovy script console the Java parent process spawns a child process that creates a Bas 64 encoded file in the temp directory subsequently this file is being decoded in this attack it is an elf binary next permissions are changed to make the binary executable finally executing this implant results in sending a shell over the network right to the attack ER over this reverse shell the attacker
