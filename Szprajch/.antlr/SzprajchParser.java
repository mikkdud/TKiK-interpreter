// Generated from c:/Users/adpaw/Studia/Semestr4/TKIK/Szprajch/Szprajch/Szprajch.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class SzprajchParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		MUL=1, DIV=2, ADD=3, SUB=4, EXP=5, MOD=6, NEQ=7, GTE=8, LTE=9, GT=10, 
		LT=11, EQ=12, AND=13, OR=14, NOT=15, COMMA=16, LPAREN=17, RPAREN=18, LEN=19, 
		VAL=20, ISNAN=21, PRINT=22, INPUT=23, LET=24, REM=25, IF=26, THEN=27, 
		ELSE=28, END=29, FUNCTION=30, RETURN=31, FOR=32, WHILE=33, REPEAT=34, 
		UNTIL=35, STEP=36, NEXT=37, TO=38, CONTINUE=39, EXIT=40, COMMENT=41, ID=42, 
		NUMBER=43, STRINGLITERAL=44, DOLLAR=45, NEWLINE=46, WS=47;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_block = 2, RULE_assignmentstmt = 3, 
		RULE_varname = 4, RULE_printstmt = 5, RULE_inputstmt = 6, RULE_ifstmt = 7, 
		RULE_elifstmt = 8, RULE_elsestmt = 9, RULE_forstmt = 10, RULE_whilestmt = 11, 
		RULE_repeatstmt = 12, RULE_continuestmt = 13, RULE_exitstmt = 14, RULE_functiondef = 15, 
		RULE_paramlist = 16, RULE_returnstmnt = 17, RULE_functioncall = 18, RULE_arglist = 19, 
		RULE_expression = 20, RULE_func = 21, RULE_string = 22, RULE_number = 23, 
		RULE_id = 24, RULE_lenfunc = 25, RULE_valfunc = 26, RULE_isnanfunc = 27;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "block", "assignmentstmt", "varname", "printstmt", 
			"inputstmt", "ifstmt", "elifstmt", "elsestmt", "forstmt", "whilestmt", 
			"repeatstmt", "continuestmt", "exitstmt", "functiondef", "paramlist", 
			"returnstmnt", "functioncall", "arglist", "expression", "func", "string", 
			"number", "id", "lenfunc", "valfunc", "isnanfunc"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'*'", "'/'", "'+'", "'-'", "'^'", "'MOD'", "'<>'", "'>='", "'<='", 
			"'>'", "'<'", "'='", null, null, null, "','", "'('", "')'", null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"'$'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "MUL", "DIV", "ADD", "SUB", "EXP", "MOD", "NEQ", "GTE", "LTE", 
			"GT", "LT", "EQ", "AND", "OR", "NOT", "COMMA", "LPAREN", "RPAREN", "LEN", 
			"VAL", "ISNAN", "PRINT", "INPUT", "LET", "REM", "IF", "THEN", "ELSE", 
			"END", "FUNCTION", "RETURN", "FOR", "WHILE", "REPEAT", "UNTIL", "STEP", 
			"NEXT", "TO", "CONTINUE", "EXIT", "COMMENT", "ID", "NUMBER", "STRINGLITERAL", 
			"DOLLAR", "NEWLINE", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Szprajch.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SzprajchParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode EOF() { return getToken(SzprajchParser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			block();
			setState(57);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public AssignmentstmtContext assignmentstmt() {
			return getRuleContext(AssignmentstmtContext.class,0);
		}
		public PrintstmtContext printstmt() {
			return getRuleContext(PrintstmtContext.class,0);
		}
		public InputstmtContext inputstmt() {
			return getRuleContext(InputstmtContext.class,0);
		}
		public IfstmtContext ifstmt() {
			return getRuleContext(IfstmtContext.class,0);
		}
		public ForstmtContext forstmt() {
			return getRuleContext(ForstmtContext.class,0);
		}
		public WhilestmtContext whilestmt() {
			return getRuleContext(WhilestmtContext.class,0);
		}
		public FunctiondefContext functiondef() {
			return getRuleContext(FunctiondefContext.class,0);
		}
		public ReturnstmntContext returnstmnt() {
			return getRuleContext(ReturnstmntContext.class,0);
		}
		public RepeatstmtContext repeatstmt() {
			return getRuleContext(RepeatstmtContext.class,0);
		}
		public ContinuestmtContext continuestmt() {
			return getRuleContext(ContinuestmtContext.class,0);
		}
		public ExitstmtContext exitstmt() {
			return getRuleContext(ExitstmtContext.class,0);
		}
		public TerminalNode COMMENT() { return getToken(SzprajchParser.COMMENT, 0); }
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(71);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LET:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(59);
				assignmentstmt();
				}
				break;
			case PRINT:
				enterOuterAlt(_localctx, 2);
				{
				setState(60);
				printstmt();
				}
				break;
			case INPUT:
				enterOuterAlt(_localctx, 3);
				{
				setState(61);
				inputstmt();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 4);
				{
				setState(62);
				ifstmt();
				}
				break;
			case FOR:
				enterOuterAlt(_localctx, 5);
				{
				setState(63);
				forstmt();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 6);
				{
				setState(64);
				whilestmt();
				}
				break;
			case FUNCTION:
				enterOuterAlt(_localctx, 7);
				{
				setState(65);
				functiondef();
				}
				break;
			case RETURN:
				enterOuterAlt(_localctx, 8);
				{
				setState(66);
				returnstmnt();
				}
				break;
			case REPEAT:
				enterOuterAlt(_localctx, 9);
				{
				setState(67);
				repeatstmt();
				}
				break;
			case CONTINUE:
				enterOuterAlt(_localctx, 10);
				{
				setState(68);
				continuestmt();
				}
				break;
			case EXIT:
				enterOuterAlt(_localctx, 11);
				{
				setState(69);
				exitstmt();
				}
				break;
			case COMMENT:
				enterOuterAlt(_localctx, 12);
				{
				setState(70);
				match(COMMENT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<TerminalNode> EOF() { return getTokens(SzprajchParser.EOF); }
		public TerminalNode EOF(int i) {
			return getToken(SzprajchParser.EOF, i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(SzprajchParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(SzprajchParser.NEWLINE, i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_block);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8279719673856L) != 0)) {
				{
				{
				setState(73);
				statement();
				setState(80);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case NEWLINE:
					{
					setState(75); 
					_errHandler.sync(this);
					_alt = 1;
					do {
						switch (_alt) {
						case 1:
							{
							{
							setState(74);
							match(NEWLINE);
							}
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						setState(77); 
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
					} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
					}
					break;
				case EOF:
					{
					setState(79);
					match(EOF);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				}
				setState(86);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentstmtContext extends ParserRuleContext {
		public VarnameContext varname() {
			return getRuleContext(VarnameContext.class,0);
		}
		public TerminalNode EQ() { return getToken(SzprajchParser.EQ, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode LET() { return getToken(SzprajchParser.LET, 0); }
		public AssignmentstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentstmt; }
	}

	public final AssignmentstmtContext assignmentstmt() throws RecognitionException {
		AssignmentstmtContext _localctx = new AssignmentstmtContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_assignmentstmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LET) {
				{
				setState(87);
				match(LET);
				}
			}

			setState(90);
			varname();
			setState(91);
			match(EQ);
			setState(92);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarnameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SzprajchParser.ID, 0); }
		public VarnameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varname; }
	}

	public final VarnameContext varname() throws RecognitionException {
		VarnameContext _localctx = new VarnameContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_varname);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintstmtContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(SzprajchParser.PRINT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public PrintstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printstmt; }
	}

	public final PrintstmtContext printstmt() throws RecognitionException {
		PrintstmtContext _localctx = new PrintstmtContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_printstmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			match(PRINT);
			setState(97);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InputstmtContext extends ParserRuleContext {
		public TerminalNode INPUT() { return getToken(SzprajchParser.INPUT, 0); }
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public VarnameContext varname() {
			return getRuleContext(VarnameContext.class,0);
		}
		public InputstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inputstmt; }
	}

	public final InputstmtContext inputstmt() throws RecognitionException {
		InputstmtContext _localctx = new InputstmtContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_inputstmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			match(INPUT);
			setState(100);
			string();
			setState(101);
			varname();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfstmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(SzprajchParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode THEN() { return getToken(SzprajchParser.THEN, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode END() { return getToken(SzprajchParser.END, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(SzprajchParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(SzprajchParser.NEWLINE, i);
		}
		public List<ElifstmtContext> elifstmt() {
			return getRuleContexts(ElifstmtContext.class);
		}
		public ElifstmtContext elifstmt(int i) {
			return getRuleContext(ElifstmtContext.class,i);
		}
		public ElsestmtContext elsestmt() {
			return getRuleContext(ElsestmtContext.class,0);
		}
		public IfstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifstmt; }
	}

	public final IfstmtContext ifstmt() throws RecognitionException {
		IfstmtContext _localctx = new IfstmtContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_ifstmt);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			match(IF);
			setState(104);
			expression(0);
			setState(108);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(105);
				match(NEWLINE);
				}
				}
				setState(110);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(111);
			match(THEN);
			setState(113); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(112);
				match(NEWLINE);
				}
				}
				setState(115); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NEWLINE );
			setState(117);
			block();
			setState(121);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(118);
					elifstmt();
					}
					} 
				}
				setState(123);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(124);
				elsestmt();
				}
			}

			setState(127);
			match(END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ElifstmtContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(SzprajchParser.ELSE, 0); }
		public TerminalNode IF() { return getToken(SzprajchParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode THEN() { return getToken(SzprajchParser.THEN, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(SzprajchParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(SzprajchParser.NEWLINE, i);
		}
		public ElifstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elifstmt; }
	}

	public final ElifstmtContext elifstmt() throws RecognitionException {
		ElifstmtContext _localctx = new ElifstmtContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_elifstmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(ELSE);
			setState(130);
			match(IF);
			setState(131);
			expression(0);
			setState(135);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(132);
				match(NEWLINE);
				}
				}
				setState(137);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(138);
			match(THEN);
			setState(140); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(139);
				match(NEWLINE);
				}
				}
				setState(142); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NEWLINE );
			setState(144);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ElsestmtContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(SzprajchParser.ELSE, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(SzprajchParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(SzprajchParser.NEWLINE, i);
		}
		public ElsestmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elsestmt; }
	}

	public final ElsestmtContext elsestmt() throws RecognitionException {
		ElsestmtContext _localctx = new ElsestmtContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_elsestmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			match(ELSE);
			setState(148); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(147);
				match(NEWLINE);
				}
				}
				setState(150); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NEWLINE );
			setState(152);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForstmtContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(SzprajchParser.FOR, 0); }
		public VarnameContext varname() {
			return getRuleContext(VarnameContext.class,0);
		}
		public TerminalNode EQ() { return getToken(SzprajchParser.EQ, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode TO() { return getToken(SzprajchParser.TO, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode NEXT() { return getToken(SzprajchParser.NEXT, 0); }
		public TerminalNode STEP() { return getToken(SzprajchParser.STEP, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(SzprajchParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(SzprajchParser.NEWLINE, i);
		}
		public ForstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forstmt; }
	}

	public final ForstmtContext forstmt() throws RecognitionException {
		ForstmtContext _localctx = new ForstmtContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_forstmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(154);
			match(FOR);
			setState(155);
			varname();
			setState(156);
			match(EQ);
			setState(157);
			expression(0);
			setState(158);
			match(TO);
			setState(159);
			expression(0);
			setState(162);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==STEP) {
				{
				setState(160);
				match(STEP);
				setState(161);
				expression(0);
				}
			}

			setState(165); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(164);
				match(NEWLINE);
				}
				}
				setState(167); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NEWLINE );
			setState(169);
			block();
			setState(170);
			match(NEXT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhilestmtContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(SzprajchParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode END() { return getToken(SzprajchParser.END, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(SzprajchParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(SzprajchParser.NEWLINE, i);
		}
		public WhilestmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whilestmt; }
	}

	public final WhilestmtContext whilestmt() throws RecognitionException {
		WhilestmtContext _localctx = new WhilestmtContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_whilestmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			match(WHILE);
			setState(173);
			expression(0);
			setState(175); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(174);
				match(NEWLINE);
				}
				}
				setState(177); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NEWLINE );
			setState(179);
			block();
			setState(180);
			match(END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RepeatstmtContext extends ParserRuleContext {
		public TerminalNode REPEAT() { return getToken(SzprajchParser.REPEAT, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode UNTIL() { return getToken(SzprajchParser.UNTIL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(SzprajchParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(SzprajchParser.NEWLINE, i);
		}
		public RepeatstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repeatstmt; }
	}

	public final RepeatstmtContext repeatstmt() throws RecognitionException {
		RepeatstmtContext _localctx = new RepeatstmtContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_repeatstmt);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			match(REPEAT);
			setState(184); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(183);
					match(NEWLINE);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(186); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(188);
			block();
			setState(192);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(189);
				match(NEWLINE);
				}
				}
				setState(194);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(195);
			match(UNTIL);
			setState(196);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ContinuestmtContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(SzprajchParser.CONTINUE, 0); }
		public ContinuestmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continuestmt; }
	}

	public final ContinuestmtContext continuestmt() throws RecognitionException {
		ContinuestmtContext _localctx = new ContinuestmtContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_continuestmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(198);
			match(CONTINUE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExitstmtContext extends ParserRuleContext {
		public TerminalNode EXIT() { return getToken(SzprajchParser.EXIT, 0); }
		public ExitstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exitstmt; }
	}

	public final ExitstmtContext exitstmt() throws RecognitionException {
		ExitstmtContext _localctx = new ExitstmtContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_exitstmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(200);
			match(EXIT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctiondefContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(SzprajchParser.FUNCTION, 0); }
		public TerminalNode ID() { return getToken(SzprajchParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(SzprajchParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(SzprajchParser.RPAREN, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode END() { return getToken(SzprajchParser.END, 0); }
		public ParamlistContext paramlist() {
			return getRuleContext(ParamlistContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(SzprajchParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(SzprajchParser.NEWLINE, i);
		}
		public FunctiondefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functiondef; }
	}

	public final FunctiondefContext functiondef() throws RecognitionException {
		FunctiondefContext _localctx = new FunctiondefContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_functiondef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			match(FUNCTION);
			setState(203);
			match(ID);
			setState(204);
			match(LPAREN);
			setState(206);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(205);
				paramlist();
				}
			}

			setState(208);
			match(RPAREN);
			setState(210); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(209);
				match(NEWLINE);
				}
				}
				setState(212); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NEWLINE );
			setState(214);
			block();
			setState(215);
			match(END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamlistContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(SzprajchParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(SzprajchParser.ID, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(SzprajchParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(SzprajchParser.COMMA, i);
		}
		public ParamlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramlist; }
	}

	public final ParamlistContext paramlist() throws RecognitionException {
		ParamlistContext _localctx = new ParamlistContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_paramlist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(217);
			match(ID);
			setState(222);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(218);
				match(COMMA);
				setState(219);
				match(ID);
				}
				}
				setState(224);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnstmntContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(SzprajchParser.RETURN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ReturnstmntContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnstmnt; }
	}

	public final ReturnstmntContext returnstmnt() throws RecognitionException {
		ReturnstmntContext _localctx = new ReturnstmntContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_returnstmnt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(225);
			match(RETURN);
			setState(226);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctioncallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SzprajchParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(SzprajchParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(SzprajchParser.RPAREN, 0); }
		public ArglistContext arglist() {
			return getRuleContext(ArglistContext.class,0);
		}
		public FunctioncallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functioncall; }
	}

	public final FunctioncallContext functioncall() throws RecognitionException {
		FunctioncallContext _localctx = new FunctioncallContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_functioncall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			match(ID);
			setState(229);
			match(LPAREN);
			setState(231);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 30786329411584L) != 0)) {
				{
				setState(230);
				arglist();
				}
			}

			setState(233);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArglistContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(SzprajchParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(SzprajchParser.COMMA, i);
		}
		public ArglistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arglist; }
	}

	public final ArglistContext arglist() throws RecognitionException {
		ArglistContext _localctx = new ArglistContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_arglist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(235);
			expression(0);
			setState(240);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(236);
				match(COMMA);
				setState(237);
				expression(0);
				}
				}
				setState(242);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AndExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode AND() { return getToken(SzprajchParser.AND, 0); }
		public AndExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StringExprContext extends ExpressionContext {
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public StringExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MulDivExprContext extends ExpressionContext {
		public Token op;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MUL() { return getToken(SzprajchParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(SzprajchParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(SzprajchParser.MOD, 0); }
		public MulDivExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IdExprContext extends ExpressionContext {
		public IdContext id() {
			return getRuleContext(IdContext.class,0);
		}
		public IdExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NumberExprContext extends ExpressionContext {
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public NumberExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RelExprContext extends ExpressionContext {
		public Token op;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode GTE() { return getToken(SzprajchParser.GTE, 0); }
		public TerminalNode GT() { return getToken(SzprajchParser.GT, 0); }
		public TerminalNode LTE() { return getToken(SzprajchParser.LTE, 0); }
		public TerminalNode LT() { return getToken(SzprajchParser.LT, 0); }
		public TerminalNode EQ() { return getToken(SzprajchParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(SzprajchParser.NEQ, 0); }
		public RelExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NotExprContext extends ExpressionContext {
		public TerminalNode NOT() { return getToken(SzprajchParser.NOT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public NotExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParenExprContext extends ExpressionContext {
		public TerminalNode LPAREN() { return getToken(SzprajchParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(SzprajchParser.RPAREN, 0); }
		public ParenExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExpExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode EXP() { return getToken(SzprajchParser.EXP, 0); }
		public ExpExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FuncExprContext extends ExpressionContext {
		public FuncContext func() {
			return getRuleContext(FuncContext.class,0);
		}
		public FuncExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AddSubExprContext extends ExpressionContext {
		public Token op;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode ADD() { return getToken(SzprajchParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(SzprajchParser.SUB, 0); }
		public AddSubExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OrExprContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode OR() { return getToken(SzprajchParser.OR, 0); }
		public OrExprContext(ExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 40;
		enterRecursionRule(_localctx, 40, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(254);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STRINGLITERAL:
				{
				_localctx = new StringExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(244);
				string();
				}
				break;
			case NUMBER:
				{
				_localctx = new NumberExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(245);
				number();
				}
				break;
			case LEN:
			case VAL:
			case ISNAN:
				{
				_localctx = new FuncExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(246);
				func();
				}
				break;
			case ID:
				{
				_localctx = new IdExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(247);
				id();
				}
				break;
			case LPAREN:
				{
				_localctx = new ParenExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				{
				setState(248);
				match(LPAREN);
				setState(249);
				expression(0);
				setState(250);
				match(RPAREN);
				}
				}
				break;
			case NOT:
				{
				_localctx = new NotExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(252);
				match(NOT);
				setState(253);
				expression(4);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(276);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(274);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
					case 1:
						{
						_localctx = new MulDivExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(256);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(257);
						((MulDivExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 70L) != 0)) ) {
							((MulDivExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(258);
						expression(8);
						}
						break;
					case 2:
						{
						_localctx = new AddSubExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(259);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(260);
						((AddSubExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
							((AddSubExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(261);
						expression(7);
						}
						break;
					case 3:
						{
						_localctx = new RelExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(262);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(263);
						((RelExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 8064L) != 0)) ) {
							((RelExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(264);
						expression(6);
						}
						break;
					case 4:
						{
						_localctx = new AndExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(265);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(266);
						match(AND);
						setState(267);
						expression(4);
						}
						break;
					case 5:
						{
						_localctx = new OrExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(268);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(269);
						match(OR);
						setState(270);
						expression(3);
						}
						break;
					case 6:
						{
						_localctx = new ExpExprContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(271);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(272);
						match(EXP);
						setState(273);
						expression(1);
						}
						break;
					}
					} 
				}
				setState(278);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncContext extends ParserRuleContext {
		public LenfuncContext lenfunc() {
			return getRuleContext(LenfuncContext.class,0);
		}
		public ValfuncContext valfunc() {
			return getRuleContext(ValfuncContext.class,0);
		}
		public IsnanfuncContext isnanfunc() {
			return getRuleContext(IsnanfuncContext.class,0);
		}
		public FuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func; }
	}

	public final FuncContext func() throws RecognitionException {
		FuncContext _localctx = new FuncContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_func);
		try {
			setState(282);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEN:
				enterOuterAlt(_localctx, 1);
				{
				setState(279);
				lenfunc();
				}
				break;
			case VAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(280);
				valfunc();
				}
				break;
			case ISNAN:
				enterOuterAlt(_localctx, 3);
				{
				setState(281);
				isnanfunc();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StringContext extends ParserRuleContext {
		public TerminalNode STRINGLITERAL() { return getToken(SzprajchParser.STRINGLITERAL, 0); }
		public StringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string; }
	}

	public final StringContext string() throws RecognitionException {
		StringContext _localctx = new StringContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_string);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(284);
			match(STRINGLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumberContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(SzprajchParser.NUMBER, 0); }
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_number);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(286);
			match(NUMBER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdContext extends ParserRuleContext {
		public FunctioncallContext functioncall() {
			return getRuleContext(FunctioncallContext.class,0);
		}
		public TerminalNode ID() { return getToken(SzprajchParser.ID, 0); }
		public IdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id; }
	}

	public final IdContext id() throws RecognitionException {
		IdContext _localctx = new IdContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_id);
		try {
			setState(290);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(288);
				functioncall();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(289);
				match(ID);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LenfuncContext extends ParserRuleContext {
		public TerminalNode LEN() { return getToken(SzprajchParser.LEN, 0); }
		public TerminalNode LPAREN() { return getToken(SzprajchParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(SzprajchParser.RPAREN, 0); }
		public LenfuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lenfunc; }
	}

	public final LenfuncContext lenfunc() throws RecognitionException {
		LenfuncContext _localctx = new LenfuncContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_lenfunc);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(292);
			match(LEN);
			setState(293);
			match(LPAREN);
			setState(294);
			expression(0);
			setState(295);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValfuncContext extends ParserRuleContext {
		public TerminalNode VAL() { return getToken(SzprajchParser.VAL, 0); }
		public TerminalNode LPAREN() { return getToken(SzprajchParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(SzprajchParser.RPAREN, 0); }
		public ValfuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_valfunc; }
	}

	public final ValfuncContext valfunc() throws RecognitionException {
		ValfuncContext _localctx = new ValfuncContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_valfunc);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(297);
			match(VAL);
			setState(298);
			match(LPAREN);
			setState(299);
			expression(0);
			setState(300);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IsnanfuncContext extends ParserRuleContext {
		public TerminalNode ISNAN() { return getToken(SzprajchParser.ISNAN, 0); }
		public TerminalNode LPAREN() { return getToken(SzprajchParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(SzprajchParser.RPAREN, 0); }
		public IsnanfuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_isnanfunc; }
	}

	public final IsnanfuncContext isnanfunc() throws RecognitionException {
		IsnanfuncContext _localctx = new IsnanfuncContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_isnanfunc);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(302);
			match(ISNAN);
			setState(303);
			match(LPAREN);
			setState(304);
			expression(0);
			setState(305);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 20:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 7);
		case 1:
			return precpred(_ctx, 6);
		case 2:
			return precpred(_ctx, 5);
		case 3:
			return precpred(_ctx, 3);
		case 4:
			return precpred(_ctx, 2);
		case 5:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001/\u0134\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001H\b\u0001\u0001\u0002"+
		"\u0001\u0002\u0004\u0002L\b\u0002\u000b\u0002\f\u0002M\u0001\u0002\u0003"+
		"\u0002Q\b\u0002\u0005\u0002S\b\u0002\n\u0002\f\u0002V\t\u0002\u0001\u0003"+
		"\u0003\u0003Y\b\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0005\u0007k\b\u0007\n\u0007\f\u0007n\t\u0007\u0001\u0007\u0001\u0007"+
		"\u0004\u0007r\b\u0007\u000b\u0007\f\u0007s\u0001\u0007\u0001\u0007\u0005"+
		"\u0007x\b\u0007\n\u0007\f\u0007{\t\u0007\u0001\u0007\u0003\u0007~\b\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0005\b\u0086"+
		"\b\b\n\b\f\b\u0089\t\b\u0001\b\u0001\b\u0004\b\u008d\b\b\u000b\b\f\b\u008e"+
		"\u0001\b\u0001\b\u0001\t\u0001\t\u0004\t\u0095\b\t\u000b\t\f\t\u0096\u0001"+
		"\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0003\n\u00a3\b\n\u0001\n\u0004\n\u00a6\b\n\u000b\n\f\n\u00a7\u0001"+
		"\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0004\u000b\u00b0"+
		"\b\u000b\u000b\u000b\f\u000b\u00b1\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\f\u0001\f\u0004\f\u00b9\b\f\u000b\f\f\f\u00ba\u0001\f\u0001\f\u0005"+
		"\f\u00bf\b\f\n\f\f\f\u00c2\t\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r"+
		"\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0003\u000f\u00cf\b\u000f\u0001\u000f\u0001\u000f\u0004\u000f\u00d3\b"+
		"\u000f\u000b\u000f\f\u000f\u00d4\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u00dd\b\u0010\n\u0010\f\u0010"+
		"\u00e0\t\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0003\u0012\u00e8\b\u0012\u0001\u0012\u0001\u0012\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0005\u0013\u00ef\b\u0013\n\u0013\f\u0013\u00f2"+
		"\t\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003"+
		"\u0014\u00ff\b\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0005\u0014\u0113\b\u0014\n\u0014\f\u0014\u0116\t\u0014"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u011b\b\u0015\u0001\u0016"+
		"\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0003\u0018"+
		"\u0123\b\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001b"+
		"\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0000\u0001"+
		"(\u001c\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018"+
		"\u001a\u001c\u001e \"$&(*,.0246\u0000\u0003\u0002\u0000\u0001\u0002\u0006"+
		"\u0006\u0001\u0000\u0003\u0004\u0001\u0000\u0007\f\u0145\u00008\u0001"+
		"\u0000\u0000\u0000\u0002G\u0001\u0000\u0000\u0000\u0004T\u0001\u0000\u0000"+
		"\u0000\u0006X\u0001\u0000\u0000\u0000\b^\u0001\u0000\u0000\u0000\n`\u0001"+
		"\u0000\u0000\u0000\fc\u0001\u0000\u0000\u0000\u000eg\u0001\u0000\u0000"+
		"\u0000\u0010\u0081\u0001\u0000\u0000\u0000\u0012\u0092\u0001\u0000\u0000"+
		"\u0000\u0014\u009a\u0001\u0000\u0000\u0000\u0016\u00ac\u0001\u0000\u0000"+
		"\u0000\u0018\u00b6\u0001\u0000\u0000\u0000\u001a\u00c6\u0001\u0000\u0000"+
		"\u0000\u001c\u00c8\u0001\u0000\u0000\u0000\u001e\u00ca\u0001\u0000\u0000"+
		"\u0000 \u00d9\u0001\u0000\u0000\u0000\"\u00e1\u0001\u0000\u0000\u0000"+
		"$\u00e4\u0001\u0000\u0000\u0000&\u00eb\u0001\u0000\u0000\u0000(\u00fe"+
		"\u0001\u0000\u0000\u0000*\u011a\u0001\u0000\u0000\u0000,\u011c\u0001\u0000"+
		"\u0000\u0000.\u011e\u0001\u0000\u0000\u00000\u0122\u0001\u0000\u0000\u0000"+
		"2\u0124\u0001\u0000\u0000\u00004\u0129\u0001\u0000\u0000\u00006\u012e"+
		"\u0001\u0000\u0000\u000089\u0003\u0004\u0002\u00009:\u0005\u0000\u0000"+
		"\u0001:\u0001\u0001\u0000\u0000\u0000;H\u0003\u0006\u0003\u0000<H\u0003"+
		"\n\u0005\u0000=H\u0003\f\u0006\u0000>H\u0003\u000e\u0007\u0000?H\u0003"+
		"\u0014\n\u0000@H\u0003\u0016\u000b\u0000AH\u0003\u001e\u000f\u0000BH\u0003"+
		"\"\u0011\u0000CH\u0003\u0018\f\u0000DH\u0003\u001a\r\u0000EH\u0003\u001c"+
		"\u000e\u0000FH\u0005)\u0000\u0000G;\u0001\u0000\u0000\u0000G<\u0001\u0000"+
		"\u0000\u0000G=\u0001\u0000\u0000\u0000G>\u0001\u0000\u0000\u0000G?\u0001"+
		"\u0000\u0000\u0000G@\u0001\u0000\u0000\u0000GA\u0001\u0000\u0000\u0000"+
		"GB\u0001\u0000\u0000\u0000GC\u0001\u0000\u0000\u0000GD\u0001\u0000\u0000"+
		"\u0000GE\u0001\u0000\u0000\u0000GF\u0001\u0000\u0000\u0000H\u0003\u0001"+
		"\u0000\u0000\u0000IP\u0003\u0002\u0001\u0000JL\u0005.\u0000\u0000KJ\u0001"+
		"\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000MK\u0001\u0000\u0000\u0000"+
		"MN\u0001\u0000\u0000\u0000NQ\u0001\u0000\u0000\u0000OQ\u0005\u0000\u0000"+
		"\u0001PK\u0001\u0000\u0000\u0000PO\u0001\u0000\u0000\u0000QS\u0001\u0000"+
		"\u0000\u0000RI\u0001\u0000\u0000\u0000SV\u0001\u0000\u0000\u0000TR\u0001"+
		"\u0000\u0000\u0000TU\u0001\u0000\u0000\u0000U\u0005\u0001\u0000\u0000"+
		"\u0000VT\u0001\u0000\u0000\u0000WY\u0005\u0018\u0000\u0000XW\u0001\u0000"+
		"\u0000\u0000XY\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000\u0000Z[\u0003"+
		"\b\u0004\u0000[\\\u0005\f\u0000\u0000\\]\u0003(\u0014\u0000]\u0007\u0001"+
		"\u0000\u0000\u0000^_\u0005*\u0000\u0000_\t\u0001\u0000\u0000\u0000`a\u0005"+
		"\u0016\u0000\u0000ab\u0003(\u0014\u0000b\u000b\u0001\u0000\u0000\u0000"+
		"cd\u0005\u0017\u0000\u0000de\u0003,\u0016\u0000ef\u0003\b\u0004\u0000"+
		"f\r\u0001\u0000\u0000\u0000gh\u0005\u001a\u0000\u0000hl\u0003(\u0014\u0000"+
		"ik\u0005.\u0000\u0000ji\u0001\u0000\u0000\u0000kn\u0001\u0000\u0000\u0000"+
		"lj\u0001\u0000\u0000\u0000lm\u0001\u0000\u0000\u0000mo\u0001\u0000\u0000"+
		"\u0000nl\u0001\u0000\u0000\u0000oq\u0005\u001b\u0000\u0000pr\u0005.\u0000"+
		"\u0000qp\u0001\u0000\u0000\u0000rs\u0001\u0000\u0000\u0000sq\u0001\u0000"+
		"\u0000\u0000st\u0001\u0000\u0000\u0000tu\u0001\u0000\u0000\u0000uy\u0003"+
		"\u0004\u0002\u0000vx\u0003\u0010\b\u0000wv\u0001\u0000\u0000\u0000x{\u0001"+
		"\u0000\u0000\u0000yw\u0001\u0000\u0000\u0000yz\u0001\u0000\u0000\u0000"+
		"z}\u0001\u0000\u0000\u0000{y\u0001\u0000\u0000\u0000|~\u0003\u0012\t\u0000"+
		"}|\u0001\u0000\u0000\u0000}~\u0001\u0000\u0000\u0000~\u007f\u0001\u0000"+
		"\u0000\u0000\u007f\u0080\u0005\u001d\u0000\u0000\u0080\u000f\u0001\u0000"+
		"\u0000\u0000\u0081\u0082\u0005\u001c\u0000\u0000\u0082\u0083\u0005\u001a"+
		"\u0000\u0000\u0083\u0087\u0003(\u0014\u0000\u0084\u0086\u0005.\u0000\u0000"+
		"\u0085\u0084\u0001\u0000\u0000\u0000\u0086\u0089\u0001\u0000\u0000\u0000"+
		"\u0087\u0085\u0001\u0000\u0000\u0000\u0087\u0088\u0001\u0000\u0000\u0000"+
		"\u0088\u008a\u0001\u0000\u0000\u0000\u0089\u0087\u0001\u0000\u0000\u0000"+
		"\u008a\u008c\u0005\u001b\u0000\u0000\u008b\u008d\u0005.\u0000\u0000\u008c"+
		"\u008b\u0001\u0000\u0000\u0000\u008d\u008e\u0001\u0000\u0000\u0000\u008e"+
		"\u008c\u0001\u0000\u0000\u0000\u008e\u008f\u0001\u0000\u0000\u0000\u008f"+
		"\u0090\u0001\u0000\u0000\u0000\u0090\u0091\u0003\u0004\u0002\u0000\u0091"+
		"\u0011\u0001\u0000\u0000\u0000\u0092\u0094\u0005\u001c\u0000\u0000\u0093"+
		"\u0095\u0005.\u0000\u0000\u0094\u0093\u0001\u0000\u0000\u0000\u0095\u0096"+
		"\u0001\u0000\u0000\u0000\u0096\u0094\u0001\u0000\u0000\u0000\u0096\u0097"+
		"\u0001\u0000\u0000\u0000\u0097\u0098\u0001\u0000\u0000\u0000\u0098\u0099"+
		"\u0003\u0004\u0002\u0000\u0099\u0013\u0001\u0000\u0000\u0000\u009a\u009b"+
		"\u0005 \u0000\u0000\u009b\u009c\u0003\b\u0004\u0000\u009c\u009d\u0005"+
		"\f\u0000\u0000\u009d\u009e\u0003(\u0014\u0000\u009e\u009f\u0005&\u0000"+
		"\u0000\u009f\u00a2\u0003(\u0014\u0000\u00a0\u00a1\u0005$\u0000\u0000\u00a1"+
		"\u00a3\u0003(\u0014\u0000\u00a2\u00a0\u0001\u0000\u0000\u0000\u00a2\u00a3"+
		"\u0001\u0000\u0000\u0000\u00a3\u00a5\u0001\u0000\u0000\u0000\u00a4\u00a6"+
		"\u0005.\u0000\u0000\u00a5\u00a4\u0001\u0000\u0000\u0000\u00a6\u00a7\u0001"+
		"\u0000\u0000\u0000\u00a7\u00a5\u0001\u0000\u0000\u0000\u00a7\u00a8\u0001"+
		"\u0000\u0000\u0000\u00a8\u00a9\u0001\u0000\u0000\u0000\u00a9\u00aa\u0003"+
		"\u0004\u0002\u0000\u00aa\u00ab\u0005%\u0000\u0000\u00ab\u0015\u0001\u0000"+
		"\u0000\u0000\u00ac\u00ad\u0005!\u0000\u0000\u00ad\u00af\u0003(\u0014\u0000"+
		"\u00ae\u00b0\u0005.\u0000\u0000\u00af\u00ae\u0001\u0000\u0000\u0000\u00b0"+
		"\u00b1\u0001\u0000\u0000\u0000\u00b1\u00af\u0001\u0000\u0000\u0000\u00b1"+
		"\u00b2\u0001\u0000\u0000\u0000\u00b2\u00b3\u0001\u0000\u0000\u0000\u00b3"+
		"\u00b4\u0003\u0004\u0002\u0000\u00b4\u00b5\u0005\u001d\u0000\u0000\u00b5"+
		"\u0017\u0001\u0000\u0000\u0000\u00b6\u00b8\u0005\"\u0000\u0000\u00b7\u00b9"+
		"\u0005.\u0000\u0000\u00b8\u00b7\u0001\u0000\u0000\u0000\u00b9\u00ba\u0001"+
		"\u0000\u0000\u0000\u00ba\u00b8\u0001\u0000\u0000\u0000\u00ba\u00bb\u0001"+
		"\u0000\u0000\u0000\u00bb\u00bc\u0001\u0000\u0000\u0000\u00bc\u00c0\u0003"+
		"\u0004\u0002\u0000\u00bd\u00bf\u0005.\u0000\u0000\u00be\u00bd\u0001\u0000"+
		"\u0000\u0000\u00bf\u00c2\u0001\u0000\u0000\u0000\u00c0\u00be\u0001\u0000"+
		"\u0000\u0000\u00c0\u00c1\u0001\u0000\u0000\u0000\u00c1\u00c3\u0001\u0000"+
		"\u0000\u0000\u00c2\u00c0\u0001\u0000\u0000\u0000\u00c3\u00c4\u0005#\u0000"+
		"\u0000\u00c4\u00c5\u0003(\u0014\u0000\u00c5\u0019\u0001\u0000\u0000\u0000"+
		"\u00c6\u00c7\u0005\'\u0000\u0000\u00c7\u001b\u0001\u0000\u0000\u0000\u00c8"+
		"\u00c9\u0005(\u0000\u0000\u00c9\u001d\u0001\u0000\u0000\u0000\u00ca\u00cb"+
		"\u0005\u001e\u0000\u0000\u00cb\u00cc\u0005*\u0000\u0000\u00cc\u00ce\u0005"+
		"\u0011\u0000\u0000\u00cd\u00cf\u0003 \u0010\u0000\u00ce\u00cd\u0001\u0000"+
		"\u0000\u0000\u00ce\u00cf\u0001\u0000\u0000\u0000\u00cf\u00d0\u0001\u0000"+
		"\u0000\u0000\u00d0\u00d2\u0005\u0012\u0000\u0000\u00d1\u00d3\u0005.\u0000"+
		"\u0000\u00d2\u00d1\u0001\u0000\u0000\u0000\u00d3\u00d4\u0001\u0000\u0000"+
		"\u0000\u00d4\u00d2\u0001\u0000\u0000\u0000\u00d4\u00d5\u0001\u0000\u0000"+
		"\u0000\u00d5\u00d6\u0001\u0000\u0000\u0000\u00d6\u00d7\u0003\u0004\u0002"+
		"\u0000\u00d7\u00d8\u0005\u001d\u0000\u0000\u00d8\u001f\u0001\u0000\u0000"+
		"\u0000\u00d9\u00de\u0005*\u0000\u0000\u00da\u00db\u0005\u0010\u0000\u0000"+
		"\u00db\u00dd\u0005*\u0000\u0000\u00dc\u00da\u0001\u0000\u0000\u0000\u00dd"+
		"\u00e0\u0001\u0000\u0000\u0000\u00de\u00dc\u0001\u0000\u0000\u0000\u00de"+
		"\u00df\u0001\u0000\u0000\u0000\u00df!\u0001\u0000\u0000\u0000\u00e0\u00de"+
		"\u0001\u0000\u0000\u0000\u00e1\u00e2\u0005\u001f\u0000\u0000\u00e2\u00e3"+
		"\u0003(\u0014\u0000\u00e3#\u0001\u0000\u0000\u0000\u00e4\u00e5\u0005*"+
		"\u0000\u0000\u00e5\u00e7\u0005\u0011\u0000\u0000\u00e6\u00e8\u0003&\u0013"+
		"\u0000\u00e7\u00e6\u0001\u0000\u0000\u0000\u00e7\u00e8\u0001\u0000\u0000"+
		"\u0000\u00e8\u00e9\u0001\u0000\u0000\u0000\u00e9\u00ea\u0005\u0012\u0000"+
		"\u0000\u00ea%\u0001\u0000\u0000\u0000\u00eb\u00f0\u0003(\u0014\u0000\u00ec"+
		"\u00ed\u0005\u0010\u0000\u0000\u00ed\u00ef\u0003(\u0014\u0000\u00ee\u00ec"+
		"\u0001\u0000\u0000\u0000\u00ef\u00f2\u0001\u0000\u0000\u0000\u00f0\u00ee"+
		"\u0001\u0000\u0000\u0000\u00f0\u00f1\u0001\u0000\u0000\u0000\u00f1\'\u0001"+
		"\u0000\u0000\u0000\u00f2\u00f0\u0001\u0000\u0000\u0000\u00f3\u00f4\u0006"+
		"\u0014\uffff\uffff\u0000\u00f4\u00ff\u0003,\u0016\u0000\u00f5\u00ff\u0003"+
		".\u0017\u0000\u00f6\u00ff\u0003*\u0015\u0000\u00f7\u00ff\u00030\u0018"+
		"\u0000\u00f8\u00f9\u0005\u0011\u0000\u0000\u00f9\u00fa\u0003(\u0014\u0000"+
		"\u00fa\u00fb\u0005\u0012\u0000\u0000\u00fb\u00ff\u0001\u0000\u0000\u0000"+
		"\u00fc\u00fd\u0005\u000f\u0000\u0000\u00fd\u00ff\u0003(\u0014\u0004\u00fe"+
		"\u00f3\u0001\u0000\u0000\u0000\u00fe\u00f5\u0001\u0000\u0000\u0000\u00fe"+
		"\u00f6\u0001\u0000\u0000\u0000\u00fe\u00f7\u0001\u0000\u0000\u0000\u00fe"+
		"\u00f8\u0001\u0000\u0000\u0000\u00fe\u00fc\u0001\u0000\u0000\u0000\u00ff"+
		"\u0114\u0001\u0000\u0000\u0000\u0100\u0101\n\u0007\u0000\u0000\u0101\u0102"+
		"\u0007\u0000\u0000\u0000\u0102\u0113\u0003(\u0014\b\u0103\u0104\n\u0006"+
		"\u0000\u0000\u0104\u0105\u0007\u0001\u0000\u0000\u0105\u0113\u0003(\u0014"+
		"\u0007\u0106\u0107\n\u0005\u0000\u0000\u0107\u0108\u0007\u0002\u0000\u0000"+
		"\u0108\u0113\u0003(\u0014\u0006\u0109\u010a\n\u0003\u0000\u0000\u010a"+
		"\u010b\u0005\r\u0000\u0000\u010b\u0113\u0003(\u0014\u0004\u010c\u010d"+
		"\n\u0002\u0000\u0000\u010d\u010e\u0005\u000e\u0000\u0000\u010e\u0113\u0003"+
		"(\u0014\u0003\u010f\u0110\n\u0001\u0000\u0000\u0110\u0111\u0005\u0005"+
		"\u0000\u0000\u0111\u0113\u0003(\u0014\u0001\u0112\u0100\u0001\u0000\u0000"+
		"\u0000\u0112\u0103\u0001\u0000\u0000\u0000\u0112\u0106\u0001\u0000\u0000"+
		"\u0000\u0112\u0109\u0001\u0000\u0000\u0000\u0112\u010c\u0001\u0000\u0000"+
		"\u0000\u0112\u010f\u0001\u0000\u0000\u0000\u0113\u0116\u0001\u0000\u0000"+
		"\u0000\u0114\u0112\u0001\u0000\u0000\u0000\u0114\u0115\u0001\u0000\u0000"+
		"\u0000\u0115)\u0001\u0000\u0000\u0000\u0116\u0114\u0001\u0000\u0000\u0000"+
		"\u0117\u011b\u00032\u0019\u0000\u0118\u011b\u00034\u001a\u0000\u0119\u011b"+
		"\u00036\u001b\u0000\u011a\u0117\u0001\u0000\u0000\u0000\u011a\u0118\u0001"+
		"\u0000\u0000\u0000\u011a\u0119\u0001\u0000\u0000\u0000\u011b+\u0001\u0000"+
		"\u0000\u0000\u011c\u011d\u0005,\u0000\u0000\u011d-\u0001\u0000\u0000\u0000"+
		"\u011e\u011f\u0005+\u0000\u0000\u011f/\u0001\u0000\u0000\u0000\u0120\u0123"+
		"\u0003$\u0012\u0000\u0121\u0123\u0005*\u0000\u0000\u0122\u0120\u0001\u0000"+
		"\u0000\u0000\u0122\u0121\u0001\u0000\u0000\u0000\u01231\u0001\u0000\u0000"+
		"\u0000\u0124\u0125\u0005\u0013\u0000\u0000\u0125\u0126\u0005\u0011\u0000"+
		"\u0000\u0126\u0127\u0003(\u0014\u0000\u0127\u0128\u0005\u0012\u0000\u0000"+
		"\u01283\u0001\u0000\u0000\u0000\u0129\u012a\u0005\u0014\u0000\u0000\u012a"+
		"\u012b\u0005\u0011\u0000\u0000\u012b\u012c\u0003(\u0014\u0000\u012c\u012d"+
		"\u0005\u0012\u0000\u0000\u012d5\u0001\u0000\u0000\u0000\u012e\u012f\u0005"+
		"\u0015\u0000\u0000\u012f\u0130\u0005\u0011\u0000\u0000\u0130\u0131\u0003"+
		"(\u0014\u0000\u0131\u0132\u0005\u0012\u0000\u0000\u01327\u0001\u0000\u0000"+
		"\u0000\u001bGMPTXlsy}\u0087\u008e\u0096\u00a2\u00a7\u00b1\u00ba\u00c0"+
		"\u00ce\u00d4\u00de\u00e7\u00f0\u00fe\u0112\u0114\u011a\u0122";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}