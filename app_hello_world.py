PHASES = {
    "phase1": {
        "name": "What is your name?",
        "fields": {
                "name": {
                "type": "text_input",
                "label": "What is your first name?",
            },
            "saint": {
            	"type": "text_input",
            	"label": "Who is your favorite saint?"
            }
        },
        "user_prompt": "My name is {name} and I love {saint}. Write a poem about my favorite saint.",
    },
}

from core_logic.main import main
if __name__ == "__main__":
      # Pass only necessary config instead of globals()
    main(config={"phases": PHASES})
    #main(config=globals())
