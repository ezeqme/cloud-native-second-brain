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
speakers: ["Golan Myers", "WithSecure"]
sched_url: https://kccncna2023.sched.com/event/1R2nv/arbitrary-code-file-execution-in-ro-fs-am-i-write-golan-myers-withsecure
youtube_search_url: https://www.youtube.com/results?search_query=Arbitrary+Code+%26+File+Execution+in+R%2FO+FS+%E2%80%93+Am+I+Write%3F+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Arbitrary Code & File Execution in R/O FS – Am I Write? - Golan Myers, WithSecure

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Chicago
- Speakers: Golan Myers, WithSecure
- Schedule: https://kccncna2023.sched.com/event/1R2nv/arbitrary-code-file-execution-in-ro-fs-am-i-write-golan-myers-withsecure
- Busca YouTube: https://www.youtube.com/results?search_query=Arbitrary+Code+%26+File+Execution+in+R%2FO+FS+%E2%80%93+Am+I+Write%3F+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Arbitrary Code & File Execution in R/O FS – Am I Write?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2nv/arbitrary-code-file-execution-in-ro-fs-am-i-write-golan-myers-withsecure
- YouTube search: https://www.youtube.com/results?search_query=Arbitrary+Code+%26+File+Execution+in+R%2FO+FS+%E2%80%93+Am+I+Write%3F+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jwdz-aYV5xE
- YouTube title: Arbitrary Code & File Execution in R/O FS – Am I Write? - Golan Myers, WithSecure
- Match score: 0.893
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/arbitrary-code-file-execution-in-r-o-fs-am-i-write/jwdz-aYV5xE.txt
- Transcript chars: 25619
- Keywords: basically, second, readon, execute, write, profile, specific, container, systems, within, looking, execution, dynamic, writable, executable, linker, termination, network

### Resumo baseado na transcript

okay hi everyone hope you're having a good uh conference so far uh my name is Golan and I'll be talking to you about um readon file systems and the execution of arbitrary code within them um so for starters my name is Goan like I said I'm a security consultant for with secure based out of London uh mostly I deal with azour and kubernetes and within sort of the cubern kubernetes space I focus more on the low-level aspect of containerization so level Linux uh as you can

### Excerpt da transcript

okay hi everyone hope you're having a good uh conference so far uh my name is Golan and I'll be talking to you about um readon file systems and the execution of arbitrary code within them um so for starters my name is Goan like I said I'm a security consultant for with secure based out of London uh mostly I deal with azour and kubernetes and within sort of the cubern kubernetes space I focus more on the low-level aspect of containerization so level Linux uh as you can see enthusiastic about anything containers if you see me down the hall feel free to grab me for a chat um so yeah quick agenda for what we'll be talking about today so we start off with what roning file systems are why we use them what kind of advantages they give us um in relation to security what does kubernetes have to do with that or rather containers in general we'll then kind of switch our hats over to the attacker's perspective have a look at what an attacker can do with a read only file system what's the sort of uh methodology there we'll then move on to three methods um of bypassing readon restrictions in order to execute our arbitrary code and then we'll briefly touch on remediation a bit of mitigation and some final thoughts and conclusions so for starters what is a readon file system so generically speaking when we talk about file systems the construct is built off of three sets of actions if you will H read write and execute readon file systems they're not really readon they also execute basically we kind of take away that ability to write now that's not a substitute to your individual file and folder permissions so in Linux discretionary access control that still applies at the file system level we can't write so the file system itself is immutable meaning you might see some files and folders that still have that right permission set you won't be able to write to it doesn't really make a difference what we what can we do with read only file systems why should we use them so read only file systems uh we're basically talking about immutability here they're more predictable they allow us to control and manage containerized applications better um threat detection becomes easier again when you kind of know what to expect you know what the construct should look like it's easier to kind of find an abnormality and then sort of the final step which is kind of what we're touching on today it makes it harder for attackers as an attacker here anyone who's ever kind of tried attacking a read
