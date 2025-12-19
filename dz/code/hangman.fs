open System

// Список слов для угадывания
let words = [
    "функциональный"
    "программирование"
    "виселица"
    "компьютер"
    "алгоритм"
    "структура"
    "переменная"
    "разработка"
    "интерфейс"
    "клавиатура"
]

// Состояние игры
type GameState = {
    Word: string
    GuessedLetters: Set<char>
    WrongAttempts: int
    MaxAttempts: int
}

// Инициализация новой игры
let newGame () =
    let random = Random()
    let word = words.[random.Next(words.Length)]
    {
        Word = word
        GuessedLetters = Set.empty
        WrongAttempts = 0
        MaxAttempts = 6
    }

// Отображение текущего состояния слова
let displayWord state =
    state.Word
    |> Seq.map (fun c ->
        if state.GuessedLetters.Contains(c) then c
        else '_'
    )
    |> Seq.toArray
    |> String

// Проверка, угадано ли слово полностью
let isWordGuessed state =
    state.Word
    |> Seq.forall (fun c -> state.GuessedLetters.Contains(c))

// Отображение виселицы
let displayHangman attempts maxAttempts =
    let stages = [
        """
         -----
         |   |
             |
             |
             |
             |
        --------
        """
        """
         -----
         |   |
         O   |
             |
             |
             |
        --------
        """
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        --------
        """
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        --------
        """
        """
         -----
         |   |
         O   |
        /|\  |
             |
             |
        --------
        """
        """
         -----
         |   |
         O   |
        /|\  |
        /    |
             |
        --------
        """
        """
         -----
         |   |
         O   |
        /|\  |
        / \  |
             |
        --------
        """
    ]
    
    let index = min attempts (stages.Length - 1)
    printfn "%s" stages.[index]
    printfn "Ошибок: %d/%d" attempts maxAttempts

// Обработка ввода буквы
let processGuess state guess =
    let guessChar = Char.ToLower(guess)
    
    // Проверяем, была ли уже такая буква
    if state.GuessedLetters.Contains(guessChar) then
        printfn "Вы уже вводили букву '%c'" guessChar
        state
    else
        let newGuessed = state.GuessedLetters.Add(guessChar)
        
        // Проверяем, есть ли такая буква в слове
        if state.Word.Contains(guessChar) then
            printfn "Правильно! Буква '%c' есть в слове." guessChar
            { state with GuessedLetters = newGuessed }
        else
            printfn "Неправильно! Буквы '%c' нет в слове." guessChar
            { 
                state with 
                    GuessedLetters = newGuessed
                    WrongAttempts = state.WrongAttempts + 1 
            }

// Отображение использованных букв
let displayUsedLetters state =
    let usedLetters = 
        state.GuessedLetters
        |> Set.toList
        |> List.sort
    
    if not usedLetters.IsEmpty then
        printf "Использованные буквы: "
        usedLetters |> List.iter (printf "%c ")
        printfn ""

// Основной игровой цикл
let rec gameLoop state =
    Console.Clear()
    
    printfn "=== Игра 'Виселица' ==="
    printfn ""
    
    displayHangman state.WrongAttempts state.MaxAttempts
    printfn ""
    
    let currentDisplay = displayWord state
    printfn "Слово: %s" currentDisplay
    printfn ""
    
    displayUsedLetters state
    printfn ""
    
    // Проверка условий окончания игры
    if isWordGuessed state then
        printfn "Поздравляем! Вы угадали слово: %s" state.Word
        printfn "Игра окончена!"
    elif state.WrongAttempts >= state.MaxAttempts then
        printfn "Игра окончена! Вы проиграли."
        printfn "Загаданное слово было: %s" state.Word
        displayHangman state.MaxAttempts state.MaxAttempts
    else
        printf "Введите букву: "
        let input = Console.ReadLine()
        
        if String.IsNullOrEmpty(input) then
            printfn "Пожалуйста, введите букву."
            Console.ReadLine() |> ignore
            gameLoop state
        else
            let guess = input.[0]
            let newState = processGuess state guess
            Console.ReadLine() |> ignore
            gameLoop newState

// Запуск игры
let startGame () =
    printfn "Добро пожаловать в игру 'Виселица'!"
    printfn "Угадайте слово по буквам. У вас есть 6 попыток."
    printfn "Нажмите любую клавишу для начала игры..."
    Console.ReadKey() |> ignore
    
    let initialState = newGame()
    gameLoop initialState

// Точка входа
[<EntryPoint>]
let main argv =
    startGame()
    0