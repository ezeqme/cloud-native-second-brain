---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Security"]
speakers: ["Natalia Reka Ivanko", "John Fastabend", "Isovalent"]
sched_url: https://kccnceu2023.sched.com/event/1Hybi/the-next-log4jshell-preparing-for-cves-with-ebpf-natalia-reka-ivanko-john-fastabend-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=The+Next+Log4jshell%3F%21+Preparing+for+CVEs+with+eBPF%21+CNCF+KubeCon+2023
slides: []
status: parsed
---

# The Next Log4jshell?! Preparing for CVEs with eBPF! - Natalia Reka Ivanko & John Fastabend, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Natalia Reka Ivanko, John Fastabend, Isovalent
- Schedule: https://kccnceu2023.sched.com/event/1Hybi/the-next-log4jshell-preparing-for-cves-with-ebpf-natalia-reka-ivanko-john-fastabend-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=The+Next+Log4jshell%3F%21+Preparing+for+CVEs+with+eBPF%21+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre The Next Log4jshell?! Preparing for CVEs with eBPF!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hybi/the-next-log4jshell-preparing-for-cves-with-ebpf-natalia-reka-ivanko-john-fastabend-isovalent
- YouTube search: https://www.youtube.com/results?search_query=The+Next+Log4jshell%3F%21+Preparing+for+CVEs+with+eBPF%21+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=u8HKg5pENj4
- YouTube title: The Next Log4jshell?! Preparing for CVEs with eBPF! - Natalia Reka Ivanko & John Fastabend
- Match score: 0.813
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/the-next-log4jshell-preparing-for-cves-with-ebpf/u8HKg5pENj4.txt
- Transcript chars: 31929
- Keywords: actually, kernel, basically, running, tetragon, network, execution, application, server, allows, cluster, process, library, course, interesting, libraries, executed, version

### Resumo baseado na transcript

hello everyone and then welcome to the last day of kubecon and thank you for coming um today we will we will talk about the next look for shell and then how can we prepare for these CVS with the help of evpf so who is speaking today my name is Natalie ivanko I'm a security product lead at ISO Island and here is with me John who is a staff software engineer tetragon lead and then a Serial maintainer at isovand so a little bit about the agenda so

### Excerpt da transcript

hello everyone and then welcome to the last day of kubecon and thank you for coming um today we will we will talk about the next look for shell and then how can we prepare for these CVS with the help of evpf so who is speaking today my name is Natalie ivanko I'm a security product lead at ISO Island and here is with me John who is a staff software engineer tetragon lead and then a Serial maintainer at isovand so a little bit about the agenda so we will start with a motivation like a quick recap like what is look for sure just in a one-on-one because I'm not a Java developer so I cannot really go in very details and then we will see like why ebpf would be the optimal solution to detect that we obviously an open source tool um tetragon and then we will Deep dive into how this solution would pick up lock for shell and then we wish you a demo and then I will finish with some further detection and then prevention techniques like how could we do detect the next log for sure because there will be many more coming so let's start with a quick one of them so what is lock for Shell it's actually a vulnerability in a Java logging Library which is licensed by apache2 and then it allows remote code execution so basically the attacker who could control the log messages that are going into an application and then is vulnerable um the attacker would be able to execute arbitrarily code loaded and then of course it affects wide range of products servers and vendors so why is it happening uh why this vulnerability actually exists so it's actually due to three features bugs whatever you want to call it and then two of them is in actual log forgery and then the third is actually a Java feature so the first one is um the look for JL Library allows you to log messages from sources that you actually don't control so for example if you're receiving data in your application it allows you to look for example usernames passwords or error codes return codes and so on the second one is it also allows you to lock for example environment variables so if you do like dollar sign curly based Java version curly base it will of course log the Java version you could do for example OS version and then it would actually log the OS version and normally what's interesting that it allows you to do that recursively so if the Java version actually that string contains under a dollar sign current base something something cannabis it will actually resolve that analog that as well and then the third one
