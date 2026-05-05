---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Networking"
themes: ["Networking"]
speakers: ["Billy McFall", "Adrián Moreno", "Red Hat"]
sched_url: https://kccnceu2021.sched.com/event/iE1S/there-is-a-new-spec-in-town-getting-to-know-the-device-information-spec-billy-mcfall-adrian-moreno-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=There+is+a+New+Spec+in+Town%3A+Getting+to+Know+the+Device+Information+Spec+CNCF+KubeCon+2021
slides: []
status: parsed
---

# There is a New Spec in Town: Getting to Know the Device Information Spec - Billy McFall & Adrián Moreno, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Networking]]
- Temas: [[Networking]]
- País/cidade: Virtual / Virtual
- Speakers: Billy McFall, Adrián Moreno, Red Hat
- Schedule: https://kccnceu2021.sched.com/event/iE1S/there-is-a-new-spec-in-town-getting-to-know-the-device-information-spec-billy-mcfall-adrian-moreno-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=There+is+a+New+Spec+in+Town%3A+Getting+to+Know+the+Device+Information+Spec+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre There is a New Spec in Town: Getting to Know the Device Information Spec.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE1S/there-is-a-new-spec-in-town-getting-to-know-the-device-information-spec-billy-mcfall-adrian-moreno-red-hat
- YouTube search: https://www.youtube.com/results?search_query=There+is+a+New+Spec+in+Town%3A+Getting+to+Know+the+Device+Information+Spec+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VZ3Ln8d9RUc
- YouTube title: There is a New Spec in Town: Getting to Know the Device Information... Billy McFall & Adrián Moreno
- Match score: 0.909
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/there-is-a-new-spec-in-town-getting-to-know-the-device-information-spe/VZ3Ln8d9RUc.txt
- Transcript chars: 15605
- Keywords: device, network, interface, interfaces, devices, basically, attachment, information, multis, plugin, container, looking, recently, working, meeting, actually, changes, address

### Resumo baseado na transcript

hey billy are you ready for our meeting hey adrian i don't see anyone else here is it just yesterday yes seems everyone else failed um if that's the case can we hold off for just a couple of minutes i'm trying a new deployment and i need a couple more minutes to get to a breaking point sure no problem um i can help if you want yeah i mean if you got time that would be great um so i've got a customer that's got some requirements i'm um all right i like it but you know that's when they're saying i'm still like new to all this and learning all these technologies i think if i went to one of these upstream communities i just get lost and feel kind of out

### Excerpt da transcript

hey billy are you ready for our meeting hey adrian i don't see anyone else here is it just yesterday yes seems everyone else failed um if that's the case can we hold off for just a couple of minutes i'm trying a new deployment and i need a couple more minutes to get to a breaking point sure no problem um i can help if you want yeah i mean if you got time that would be great um so i've got a customer that's got some requirements i'm not real familiar with they've got a legacy application they want to containerize and require some additional interfaces to make it work properly now i know multicni will allow you to run multiple cnis for a container which will basically add multiple interfaces to the container but the first time i've really had to do it with srv vfs i was able to bring up the pod but i can't tell which of the differential interfaces is used for what okay uh do you have a diagram or something can you show me what you're trying to do um yeah i think i got one here um all right i'm gonna i'm gonna share my screen hold on just a second i found it all right sharing can you see the drawing yes okay so as you can see from the picture they need a high speed interface to receive some video stream in on one interface the app does its transcoding magic and then sends a modified stream out a second interface these video streams are at high data rates and need to be on separate interfaces okay um i have a 5g case that is quite similar um at least uh the interfaces uh interface requirements is similar enough in fact this kind of setups is more common than you think um let's take a look at your cluster do you have uh a terminal around let's see yeah actually um i'll share but let me send you some here here's the login stuff and um now you can maybe tmux in here let me share it there we go yep yep man um so here's what i have so far i found some srv documentation so i've got enough that i was able to take my srv capable nic and divide it into multiple virtual functions so that multiple containers can share the same nic hang on i got this command and somewhere one of my notepads all right there you go so now you can see um i've got these two interfaces with four vf's each all right so now if i show you my queues gl good pawns all right so there's my test pod and um if we go and look at it so you can see here i've got e0 for my default network and then a couple of net interfaces for the additional interfaces but i don't know which net net one or niche two is us
